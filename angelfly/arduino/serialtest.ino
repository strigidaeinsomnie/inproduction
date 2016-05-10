byte c = 0;

void setup(){
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop(){
  while (Serial.available()){
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
