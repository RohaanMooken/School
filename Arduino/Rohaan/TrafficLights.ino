// C++ code
//

int REDONE = 2;
int REDTWO = 5;
int YELLOWONE = 3;
int YELLOWTWO = 6;
int GREENONE = 4;
int GREENTWO = 7;

void OneOn()
{
  digitalWrite(YELLOWONE, HIGH);
  delay(500);
  digitalWrite(GREENONE, LOW);
  delay(500);
  digitalWrite(YELLOWONE, LOW);
  digitalWrite(REDONE, HIGH);

  digitalWrite(YELLOWTWO, HIGH);
  delay(500);
  digitalWrite(REDTWO, LOW);
  delay(500);
  digitalWrite(YELLOWTWO, LOW);
  digitalWrite(GREENTWO, HIGH);
}

void TwoOn()
{
  digitalWrite(YELLOWTWO, HIGH);
  delay(500);
  digitalWrite(GREENTWO, LOW);
  delay(500);
  digitalWrite(YELLOWTWO, LOW);
  digitalWrite(REDTWO, HIGH);

  digitalWrite(YELLOWONE, HIGH);
  delay(500);
  digitalWrite(REDONE, LOW);
  delay(500);
  digitalWrite(YELLOWONE, LOW);
  digitalWrite(GREENONE, HIGH);
}
  
void setup()
{
  pinMode(REDONE, OUTPUT);
  pinMode(REDTWO, OUTPUT);
  pinMode(YELLOWONE, OUTPUT);
  pinMode(YELLOWTWO, OUTPUT);
  pinMode(GREENONE, OUTPUT);
  pinMode(GREENTWO, OUTPUT);
}

void loop()
{
  OneOn();
  delay(5000);
  TwoOn();
  delay(5000);
}
