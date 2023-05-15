int REDONE = 2;
int REDTWO = 5;
int YELLOWONE = 3;
int YELLOWTWO = 6;
int GREENONE = 4;
int GREENTWO = 7;

int BUTTONPIN = 8;

int buttonState = 0;

void OneOn()
{
  // Turn to red
  digitalWrite(YELLOWONE, HIGH);
  digitalWrite(GREENONE, LOW);
  delay(1500);
  digitalWrite(YELLOWONE, LOW);
  digitalWrite(REDONE, HIGH);

  delay(2000);

  // Turn to green
  digitalWrite(YELLOWTWO, HIGH);
  delay(1500);
  digitalWrite(REDTWO, LOW);
  digitalWrite(YELLOWTWO, LOW);
  digitalWrite(GREENTWO, HIGH);
}

void TwoOn()
{
  // Turn to red
  digitalWrite(YELLOWTWO, HIGH);
  digitalWrite(GREENTWO, LOW);
  delay(1500);
  digitalWrite(YELLOWTWO, LOW);
  digitalWrite(REDTWO, HIGH);

  delay(2000);

  // Turn to green
  digitalWrite(YELLOWONE, HIGH);
  delay(1500);
  digitalWrite(REDONE, LOW);
  digitalWrite(YELLOWONE, LOW);
  digitalWrite(GREENONE, HIGH);
}
  
void WalkingPerson()
{
  digitalWrite(YELLOWTWO, HIGH);
  digitalWrite(YELLOWONE, HIGH);
  delay(500);
  digitalWrite(GREENTWO, LOW);
  digitalWrite(GREENONE, LOW);
  delay(500);
  digitalWrite(YELLOWTWO, LOW);
  digitalWrite(YELLOWONE, LOW);
  digitalWrite(REDTWO, HIGH);
  digitalWrite(REDONE, HIGH);
  delay(1000);
}

void setup()
{
  pinMode(REDONE, OUTPUT);
  pinMode(REDTWO, OUTPUT);
  pinMode(YELLOWONE, OUTPUT);
  pinMode(YELLOWTWO, OUTPUT);
  pinMode(GREENONE, OUTPUT);
  pinMode(GREENTWO, OUTPUT);
  
  pinMode(BUTTONPIN, INPUT);
  Serial.begin(9600);
}

void loop()
{
  buttonState = digitalRead(BUTTONPIN);
  
  if (buttonState == HIGH)
  {
    WalkingPerson();
    delay(5000);
  }
  else
  {
    OneOn();
    delay(10000);
    TwoOn();
    delay(10000); 
  }
}
