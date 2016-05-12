#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3);

byte c = 0;

void setup(){
  Serial.begin(4800);
  mySerial.begin(9600);

}

void loop(){
  while (mySerial.available()){
    c = (int)Serial.read();
    //Serial.flush();
    switch(c){
      case 48://0
        digitalWrite(13,LOW);
        break;
      case 49://1
        digitalWrite(13,HIGH);
        break;
    }
  }
}
