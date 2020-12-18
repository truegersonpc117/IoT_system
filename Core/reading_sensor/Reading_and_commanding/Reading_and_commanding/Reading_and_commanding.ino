
const int ledPin = 13;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second to get an estimate of the value the arduino is reading:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}


void loop() {
  
  int sensorValue = analogRead(A0);
  
  //Serial.println(sensorValue);
  if (sensorValue>=200) {
    Serial.println("off");
    digitalWrite(ledPin, LOW);
  } else {
    Serial.println("on");
    digitalWrite(ledPin, HIGH);
  }
}
