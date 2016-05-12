#include <SoftwareSerial.h>
SoftwareSerial SerialforPrint(2, 3);

byte Can1[] = {0x18};
char input[30];
int i = 0;

void setup(){
  Serial.begin(9600);
  SerialforPrint.begin(9600);
  SerialforPrint.write(Can1, 1);
}

void loop() {
  if (Serial.available()) {
    input[i] = Serial.read();

    if (i > 30 || input[i] == '.') {
      input[i] = '\0';
      SerialforPrint.print(input);
      i = 0;
    }
    else { i++; }
  }
}
