#include <Wire.h>
#include "MAX30105.h"
#include "spo2_algorithm.h"

MAX30105 particleSensor;
uint32_t redBuffer;
uint32_t irBuffer;
int hrBuffer;
byte sensorHR;

String infoToPrint;
int readings;
bool buttonState;
bool lastButtonState;

void setup() {
  Serial.begin(9600); // initialize serial communication at 115200 bits per second:
  
  sensorHR = 0;
  // Initialize sensor
  while (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
  {
    Serial.println(F("MAX30102 was not found. Please check wiring/power."));
  }
  byte ledBrightness = 60; //Options: 0=Off to 255=50mA
  byte sampleAverage = 4; //Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  byte sampleRate = 100; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 411; //Options: 69, 118, 215, 411
  int adcRange = 4096; //Options: 2048, 4096, 8192, 16384
  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange); //Configure sensor with these settings

  infoToPrint.reserve(50);

  pinMode(4, INPUT);
  //pinMode(5, INPUT);
  readings = -1;

  buttonState = false;
  lastButtonState = false;
}

void readSensors(){
  while (particleSensor.available() == false) //do we have new data?
      particleSensor.check();
   redBuffer = particleSensor.getRed();
   irBuffer = particleSensor.getIR();
   hrBuffer = analogRead(sensorHR);
   
   //Concatenate string
   infoToPrint = "HR: ";
   infoToPrint += hrBuffer;
   
   infoToPrint += " |RedB: ";
   infoToPrint += redBuffer;
   
   infoToPrint += " |IrB: ";
   infoToPrint += irBuffer;

   infoToPrint += " |Ms: ";
   infoToPrint += millis();

   Serial.println(infoToPrint);
}

void loop() {
  //Iniciar lectura con botón
  buttonState = digitalRead(4);
  if (buttonState != lastButtonState){
    if (buttonState == LOW){
      Serial.println("Transmit");
      readings = 100; 
    }
  }
  // Para cambiar lo del button state
  lastButtonState = buttonState;
  
  //Leer o nel
  if (readings > 0){
    readSensors(); 
    readings -= 1;
    //Serial.println(readings);
  }else if (readings == 0){
    Serial.println("Endtrans");
    readings = -1;
  }else{
    Serial.println("Esperando Boton");
  }
  
}
