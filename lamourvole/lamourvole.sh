#!/bin/sh

sleeptime=420

cd lamourvole

python lamourvole.py
cat lamourvole.txt | mpage -1 - > lamourvole.ps
fax make lamourvole.ps
fax send 08051461867 lamourvole.ps.0*

while :
do
  python lamourvole.py
  sleep 42
  while :
  do

    if [ $SECONDS < $sleeptime ]
      then
      sleep 1

    else
      cat lamourvole.txt | mpage -1 - > lamourvole.ps
      fax make lamourvole.ps
      fax send 08051461867 lamourvole.ps.0*
      SECONDS=0
      break
    fi
  done

done

reboot

exit 0
