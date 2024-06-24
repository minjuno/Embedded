#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <Servo.h>

#define DHTPIN 8
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
Servo Serv1;
Servo Serv2;

int pinIR = 5;
int pinServo1 = 3;
int pinServo2 = 4;
const int ledPin = 2;

int servoAngle = 0;
int opwd = 10;
int clwd = 160;
int val = 0;
float hum;
float temp;

unsigned long lastDHTReadTime = 0;
unsigned long dhtInterval = 2000;

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serv1.attach(pinServo1);
  Serv1.write(opwd);
  Serv2.attach(pinServo2);
  Serv2.write(servoAngle);
  pinMode(pinIR, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - lastDHTReadTime >= dhtInterval) {
    lastDHTReadTime = currentMillis;

    hum = dht.readHumidity();
    temp = dht.readTemperature();

    if (!isnan(hum) && !isnan(temp)) {
      Serial.print("Temperature: ");
      Serial.print(temp);
      Serial.print(" C");
      Serial.print(" Humidity: ");
      Serial.print(hum);
      Serial.println(" %");
    } else {
      Serial.println("Failed to read from DHT sensor!");
    }
  }

  // Read IR sensor value
  val = digitalRead(pinIR);
 
  // Handle serial commands
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "TOGGLE") {
      digitalWrite(ledPin, !digitalRead(ledPin));
    }
    if (command == "TOGGLE1") {
      servoAngle = (servoAngle == 0) ? 90 : 0;
      Serv2.write(servoAngle);
    }
    if (command == "TOGGLE2") {
      opwd = (opwd == 10) ? 160 : 10;
      Serv1.write(opwd);
    }      
  }
    val = digitalRead(pinIR);
    if (val == 0) {
     
     
      Serv1.write(clwd);
    } else {
     
     
      Serv1.write(opwd);
    }
 
}
