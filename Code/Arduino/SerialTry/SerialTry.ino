// #include 
long cincuenta = 50;

void setup(){
    //Bit Transfer rate
    Serial.begin(9600);

    //Seed de random en la entrada análoga
    // Necesita que no haya nada conectado para funcionar.
    
    randomSeed(analogRead(0));
}

void loop(){
    //Números random
    int num = random (70, 100);
    Serial.println(num);
    delay(100);

}
