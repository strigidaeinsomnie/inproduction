# -*- coding: utf-8 -*-
import sys
import string
import base64
import urllib.request
import json
import wave

# service URL
tts_url ='http://rospeex.ucri.jgn-x.jp/nauth_json/jsServices/VoiceTraSS'

tts_command = { "method":"speak","params":["1.1",
    {"language":"ja","text":"こんにちは","voiceType":"F117","audioType":"audio/x-wav"}]}

obj_command = json.dumps(tts_command)     # string to json object
obj_command = obj_command.encode('utf-8')
req = urllib.request.Request(tts_url, obj_command)
response = urllib.request.urlopen(req)
received = response.read().decode('utf-8')    # get data from server

# extract wav file
obj_received = json.loads(received)
tmp = obj_received['result']['audio'] # extract result->audio
speech = base64.decodestring(tmp.encode('utf-8'))

f = open ("out.wav",'wb')
f.write(speech)
f.close
