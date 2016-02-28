#include "elapsedMillis/elapsedMillis.h"

/*The air freshener has a 15 second minimum
The on cycle is 15 seconds, meaning that you have to turn it on 15 //seconds prior to when you expect it to.
*/ 

bool canRun = true;

int secToMilli = 1000;

elapsedMillis timer0;

unsigned long sprayInterval = 0; //default at 0. Change over web app


void setup() {
    
    pinMode(ledPin1, OUTPUT);
    pinMode(D5, OUTPUT);
    
    Particle.function("led", runSys);
    
    timer0 = 0;
    
}

void loop() {
    
    if(canRun){
    
        if (timer0 > (sprayInterval - 15000)) { //time to turn on the sprayer
          
           digitalWrite(D5, HIGH);
           
           if(timer0 > (sprayInterval + 2000)) { //It has sprayed by this point, we wil turn it off. Added a bit just in case
              digitalWrite(D5, LOW);
              timer0 = 0; //timer is reset
              
           }
           
        }
      
    }
    
}



int runSys(String command) {
    
    //commands come as 0,1,3, or 6
    digitalWrite(D2, HIGH);
    delay(50);
    digitalWrite(D2, LOW);
    
    
    if(command == "0"){
    
        canRun = false;
    
        return 0;
    }
    
    if(command == "3"){
        
        canRun = true;
    
        sprayInterval =  20 * secToMilli;
        
        timer0 = 0;
   
    
        return command.toInt();
    }
    
     if(command == "6"){
        
        canRun = true;
    
        sprayInterval = 40 * secToMilli;
        //40 sec interval
    
        timer0 = 0;
   
    
        return command.toInt();
    }
    
     if(command == "9"){
        
        canRun = true;
    
        sprayInterval = 60 * secToMilli;
        //60sec interval
    
        timer0 = 0;
   
        return command.toInt();
    }
    
    return -1;
    
}

