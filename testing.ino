// defines pins numbers
const int trigPin1 = 10;// blue bin
const int echoPin1 = 11;// blue bin
const int trigPin2 = 8; // pink bin
const int echoPin2 = 9; // pink bin
// defines variables
long duration ,distance ,RightSensor,
BackSensor,FrontSensor,LeftSensor;
//long duration1;
//int distance1;

void setup() {
Serial.begin (9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);
}
void loop() {
SonarSensor(trigPin1, echoPin1); // blue bin
RightSensor = distance;
SonarSensor(trigPin2, echoPin2); // pink bin
LeftSensor = distance;
//SonarSensor(trigPin3, echoPin3);
//FrontSensor = distance;

Serial.print("0 ");
Serial.println(LeftSensor);

Serial.print("1 ");
Serial.println(RightSensor);
delay(100);

}

void SonarSensor(int trigPin,int echoPin)
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = duration*0.034/2;

}
