// light one 
int red1 = 10; 
int yellow1 = 9; 
int green1 = 8; 
// light two 
int red2 = 13; 
int yellow2 = 12; 
int green2 = 11; 

// walk button
int walkgreen = 6;
int walkred = 5;

int buttonPin = 7;
int buttonState = 0;

void ButtonCheck()
{
  buttonState = HIGH;
}

void setup() { 
  	pinMode(buttonPin, INPUT);
  	Serial.begin(9600);
	// light one 
	pinMode(red1, OUTPUT); 
	pinMode(yellow1, OUTPUT); 
	pinMode(green1, OUTPUT); 
	// light two 
	pinMode(red2, OUTPUT); 
	pinMode(yellow2, OUTPUT); 
	pinMode(green2, OUTPUT); 
  	// walk light
  	pinMode(walkgreen, OUTPUT);
  	pinMode(walkred, OUTPUT);
  	
  	attachInterrupt(digitalPinToInterrupt(buttonPin), ButtonCheck, RISING);
}

void changeLights() { 
	// turn both yellows on 
	digitalWrite(green1, LOW); 
	digitalWrite(yellow1, HIGH); 
	digitalWrite(yellow2, HIGH); 
	delay(5000); 
	// turn both yellows off, and opposite green and red 
	digitalWrite(yellow1, LOW); 
	digitalWrite(red1, HIGH); 
	digitalWrite(yellow2, LOW); 
	digitalWrite(red2, LOW); 
	digitalWrite(green2, HIGH); 
	delay(5000); 
	// both yellows on again 
	digitalWrite(yellow1, HIGH); 
	digitalWrite(yellow2, HIGH); 
	digitalWrite(green2, LOW); 
	delay(3000); 
	// turn both yellows off, and opposite green and red 
	digitalWrite(green1, HIGH); 
	digitalWrite(yellow1, LOW); 
	digitalWrite(red1, LOW); 
	digitalWrite(yellow2, LOW); 
	digitalWrite(red2, HIGH); 
	delay(5000); 
}

void walkingPerson() {
	digitalWrite(walkgreen, HIGH);
	digitalWrite(yellow2, HIGH);
	digitalWrite(yellow1, HIGH);
	delay(500);
	digitalWrite(green2, LOW);
	digitalWrite(green1, LOW);
	delay(500);
	digitalWrite(yellow2, LOW);
	digitalWrite(yellow1, LOW);
	digitalWrite(walkred, LOW);
	digitalWrite(red2, HIGH);
	digitalWrite(red1, HIGH);
}

void loop()
{
  if (buttonState == HIGH)
  {
    walkingPerson();
    buttonState = LOW;  // Reset buttonState after executing the WalkingPerson function
  }
  else
  {
    changeLights();
  }
}

