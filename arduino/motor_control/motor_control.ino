// Motor Control Pins
const int leftMotorPin1 = 2;
const int leftMotorPin2 = 3;
const int rightMotorPin1 = 4;
const int rightMotorPin2 = 5;


const int leftEnablePin = 9;
const int rightEnablePin = 10;

int motorSpeed = 200;

void setup() {
  // Initialize motor control pins as outputs
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);

  // Initialize enable pins for PWM speed control
  pinMode(leftEnablePin, OUTPUT);
  pinMode(rightEnablePin, OUTPUT);
}

void loop() {
  // Move forward
  moveForward();
  delay(1000);

  // Stop
  stopMotors();
  delay(500);

  // Move backward
  moveBackward();
  delay(1000);

  // Stop
  stopMotors();
  delay(500);

  // Turn left
  turnLeft();
  delay(1000);

  // Stop
  stopMotors();
  delay(500);

  // Turn right
  turnRight();
  delay(1000);

  // Stop
  stopMotors();
  delay(500);
}

void moveForward() {
  analogWrite(leftEnablePin, motorSpeed);
  analogWrite(rightEnablePin, motorSpeed);
  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
  digitalWrite(rightMotorPin1, HIGH);
  digitalWrite(rightMotorPin2, LOW);
}

void moveBackward() {
  analogWrite(leftEnablePin, motorSpeed);
  analogWrite(rightEnablePin, motorSpeed);
  digitalWrite(leftMotorPin1, LOW);
  digitalWrite(leftMotorPin2, HIGH);
  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, HIGH);
}

void turnLeft() {
  analogWrite(leftEnablePin, motorSpeed);
  analogWrite(rightEnablePin, motorSpeed);
  digitalWrite(leftMotorPin1, LOW);
  digitalWrite(leftMotorPin2, HIGH);
  digitalWrite(rightMotorPin1, HIGH);
  digitalWrite(rightMotorPin2, LOW);
}

void turnRight() {
  analogWrite(leftEnablePin, motorSpeed);
  analogWrite(rightEnablePin, motorSpeed);
  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, HIGH);
}

void stopMotors() {
  digitalWrite(leftMotorPin1, LOW);
  digitalWrite(leftMotorPin2, LOW);
  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, LOW);
}
