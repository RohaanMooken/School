void setup(){                   #Gjør rede for alle diodene
    pinMode(led1r, OUTPUT)
    pinMode(led1gu, OUTPUT)
    pinMode(led1gr, OUTPUT)
    pinMode(led2r, OUTPUT)
    pinMode(led2gu, OUTPUT)
    pinMode(led2gr, OUTPUT)
    pinMode(led3r, OUTPUT)
    pinMode(led3gu, OUTPUT)
    pinMode(led3gr, OUTPUT)
    pinMode(led4r, OUTPUT)
    pinMode(led4gu, OUTPUT)
    pinMode(led4gr, OUTPUT)
    pinMode(led11r, OUTPUT)
    pinMode(led12r, OUTPUT)
    pinMode(led11gr, OUTPUT)
    pinMode(led12gr, OUTPUT)
    pinMode(led21r, OUTPUT)
    pinMode(led22r, OUTPUT)
    pinMode(led21gr, OUTPUT)
    pinMode(led22gr, OUTPUT)
    pinMode(led31r, OUTPUT)
    pinMode(led32r, OUTPUT)
    pinMode(led31gr, OUTPUT)
    pinMode(led32gr, OUTPUT)
    pinMode(led41r, OUTPUT)
    pinMode(led42r, OUTPUT)
    pinMode(led41gr, OUTPUT)
    pinMode(led42gr, OUTPUT)
}
void loop(){
    if knapp1 or knapp2 or knapp5 or knapp6 = ON;       #Grønn mann hvis en av knappene til tilhørende trafikklys trykkes
        digitalWrite(led1r, HIGH);
        digitalWrite(led3r, HIGH);
        delay(1000);
        digitalWrite(led11g, HIGH);
        digitalWrite(led12g, HIGH);
        digitalWrite(led31g, HIGH);
        digitalWrite(led32g, HIGH);
        delay(7000)
        digitalWrite(led11g, LOW);
        digitalWrite(led12g, LOW);
        digitalWrite(led31g, LOW);
        digitalWrite(led32g, LOW);        
    elif knapp3 or knapp4 or knapp7 or knapp8 = ON;      #Grønn mann hvis en av knappene til tilhørende trafikklys trykkes
        digitalWrite(led2r, HIGH);
        digitalWrite(led4r, HIGH);
        delay(1000);
        digitalWrite(led21g, HIGH);
        digitalWrite(led22g, HIGH);
        digitalWrite(led41g, HIGH);
        digitalWrite(led42g, HIGH);
        delay(7000);

        digitalWrite(led21g, LOW);
        digitalWrite(led22g, LOW);
        digitalWrite(led41g, LOW);
        digitalWrite(led42g, LOW);
    elif knapp1 && knapp2 || knapp5 and knapp6 = OFF;     #Mønster til motståendetrafikklys
        digitalWrite(led11r, HIGH);
        digitalWrite(led12r, HIGH);
        digitalWrite(led31r, HIGH);
        digitalWrite(led32r, HIGH);
        digitalWrite(led1r, HIGH);
        digitalWrite(led3r, HIGH);
        delay(2000);
        digitalWrite(led1gu, HIGH);
        digitalWrite(led3gu, HIGH);
        delay(3000);
        digitalWrite(led1gu, OW);
        digitalWrite(led3gu, LOW);
        digitalWrite(led1r, LOW);
        digitalWrite(led3r, LOW); 
        digitalWrite(led1gr, HIGH);
        digitalWrite(led3gr, HIGH);
        delay(5000); 
        digitalWrite(led1gr, LOW);
        digitalWrite(led3gr, LOW); 
        digitalWrite(led1r, LOW);
        digitalWrite(led3r, LOW); 
        digitalWrite(led1gu, HIGH);
        digitalWrite(led3gu, HIGH);
        delay(3000); 

    elif knapp3 and knapp4 and knapp7 and knapp8 = OFF;     #Mønster til motståendetrafikklys
        digitalWrite(led21r, HIGH);
        digitalWrite(led22r, HIGH);
        digitalWrite(led41r, HIGH);
        digitalWrite(led42r, HIGH);
        digitalWrite(led2gr, HIGH);
        digitalWrite(led4gr, HIGH);
        delay(5000); 
        digitalWrite(led2gr, LOW);
        digitalWrite(led4gr, LOW); 
        digitalWrite(led2gu, HIGH);
        digitalWrite(led4gu, HIGH);
        delay(3000);
        digitalWrite(led2gu, LOW);
        digitalWrite(led4gu, LOW);  
        digitalWrite(led2r, HIGH);
        digitalWrite(led4r, HIGH);
        delay(2000);
        digitalWrite(led2gu, HIGH);
        digitalWrite(led4gu, HIGH);
        delay(3000);

        digitalWrite(led2r, LOW);
        digitalWrite(led4r, LOW); 
        digitalWrite(led2gu, LOW);
        digitalWrite(led4gu, LOW);
 
}
