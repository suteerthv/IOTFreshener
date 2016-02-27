// This #include statement was automatically added by the Particle IDE.
#include "elapsedMillis/elapsedMillis.h"

// This #include statement was automatically added by the Particle IDE.
#include "TimeAlarms/TimeAlarms.h"

Servo servo;

int servoPin = D0;
int relayPin = D2;
int ledPin1 = D7;
bool canRun = false;
#define minToMilli 60000;


elapsedMillis timer0;

unsigned long sprayInterval = 10 * minToMilli; //default 10 minutes


void setup() {
    
    servo.attach(servoPin);
    
    pinMode(ledPin1, OUTPUT);
    pinMode(relayPin, OUTPUT);
    
    Particle.function("led", runLED);
    
    timer0 = 0;

}

void loop() {
    
    if (timer0 > sprayInterval) {
        timer0 -= sprayInterval; //reset the timer
    
    if(canRun){
        runLEDLight();
    
        }
    }
}

void runAirFreshener() {
   
    digitalWrite(relayPin, HIGH);
    
    servo.write(0);
    
    delay(1000);
    
    servo.write(180);
    
    delay(1000);
    
    digitalWrite(relayPin, LOW);


}


void runLEDLight() {
    
    digitalWrite(ledPin1, HIGH);
    
    delay(2000);
    
    digitalWrite(ledPin1, LOW);
    
    
}

int runLED(String command) {
    
    //commands come as minutes
    
    if(command == "0"){
    
        canRun = false;
    
        return 0;
    }
    
    if(command != "0"){
        
        canRun = true;
    
        sprayInterval = command.toInt() * minToMilli;
    
        timer0 = 0;
    
        return command.toInt();
    }
    
    return -1;
    
}

