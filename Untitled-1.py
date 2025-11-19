  const int ledPin = 13; 

  void setup() {
      Serial.begin(9600);
      pinMode(ledPin, OUTPUT);
  }

  void loop() {
      if (Serial.available()) {
          String command = Serial.readStringUntil('\n');
          if (command == "ON") {
              digitalWrite(ledPin, HIGH);
          } else if (command == "OFF") {
              digitalWrite(ledPin, LOW);
          }
      }
  }
  