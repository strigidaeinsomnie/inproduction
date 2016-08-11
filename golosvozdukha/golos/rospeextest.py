# -*- coding: utf-8 -*-
import sys
import string
import base64
import urllib.request
import json
import wave
import mmap
import pyaudio

# service URL
tts_url ='http://rospeex.ucri.jgn-x.jp/nauth_json/jsServices/VoiceTraSS'

# main
if __name__=='__main__':
    # wave file
    def printWaveInfo(wf):
      # wave info
      print("channels:", wf.getnchannels())
      print("sampling width:", wf.getsampwidth())
      print("sampling rate:", wf.getframerate())
      print("frames:", wf.getnframes())
      print("params:", wf.getparams())
      print("length(sec):", float(wf.getnframes()) / wf.getframerate())

    # command
    message = sys.argv[1]
    print(message)

    tts_command = { "method":"speak",
    "params":["1.1",
    {"language":"ja","text":message,"voiceType":"F128","audioType":"audio/x-wav"}]}

    obj_command = json.dumps(tts_command)     # string to json object
    obj_command = obj_command.encode('utf-8')
    req = urllib.request.Request(tts_url, obj_command)
    response = urllib.request.urlopen(req)
    received = response.read().decode('utf-8')    # get data from server

    # extract wav file
    obj_received = json.loads(received)
    tmp = obj_received['result']['audio'] # extract result->audio
    speech = base64.decodestring(tmp.encode('utf-8'))

    # data to mmap
    speechMap = mmap.mmap(-1,len(speech))
    speechMap.write(speech)
    speechMap.seek(0)

    wf = wave.open(speechMap, 'rb')
    printWaveInfo(wf)

    # stream open
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                  channels=wf.getnchannels(),
                  rate=wf.getframerate(),
                  output=True)

    # output streams
    chunk = 1024
    data = wf.readframes(chunk)
    while data != '':
      stream.write(data)
      data = wf.readframes(chunk)
    stream.close()
    p.terminate()

    speechMap.close()
