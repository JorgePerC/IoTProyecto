

//Connections:
byte HR_S = 0;

//Global variables
int hrReading;
String line;

void setup(){
    Serial.begin(9600);
    line.reserve(50);
}


void loop(){
    hrReading = analogRead(HR_S);
    line = hrReading;
    line += "|Ms: ";
    line += millis();
    
    Serial.println(line);
}
