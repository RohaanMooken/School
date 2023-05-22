const int REDONE = 8;
const int REDTWO = 5;
const int YELLOWONE = 3;
const int YELLOWTWO = 6;
const int GREENONE = 4;
const int GREENTWO = 7;

const int BUTTONPIN = 2;

int buttonState = 0;

void ButtonCheck()
{
  buttonState = HIGH;
}

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
  Serial.print("hi");
  delay(5000);
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
  attachInterrupt(digitalPinToInterrupt(BUTTONPIN), ButtonCheck, RISING);
  Serial.begin(9600);
}

void loop()
{
  if (buttonState == HIGH)
  {
    WalkingPerson();
    buttonState = LOW;  // Reset buttonState after executing the WalkingPerson function
  }
  else
  {
    OneOn();
    delay(5000);
    TwoOn();
    delay(5000);
  }
}
