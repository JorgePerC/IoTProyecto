
//Connections:
byte HR_S = 0;

void setup(){
    Serial.begin(9600);
}


int hrReading;
void loop(){
    hrReading = analogRead(HR_S);
    Serial.println(hrReading);
    delay(100);

}
