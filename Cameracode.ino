#include <Servo.h>          // servo library
Servo servo1;              // create servo object for servo1
int number;                // declare variable 
int degree = 90;           // declare and set variable to 90 degrees

void setup()
{
  Serial.begin(9600);      // standard commuincation speed
  servo1.attach(9);        // attaches the servo on pin 9 to the servo object
  servo1.write(degree);    // put servo1 at 90 degree position 
}
void loop()
{
  while(Serial.available()){   // while serial port has data to read
  number = Serial.read();      // read in serial data and put in number variable
  if(number < 50){             // check number is less than 50
    servo1.write(degree=degree+1);  // move servo1 to the left(from camera point of view) until face is centered
    delay(20);}                // pause to give servo time to move
  else{
    servo1.write(degree=degree-1);  // move servo1 to the right(from camera point of view) until face is centered
    delay(20);}                // pause to give servo time to move
  };
}

