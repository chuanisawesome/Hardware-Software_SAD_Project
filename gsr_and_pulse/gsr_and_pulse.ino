
#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library. 


// this is for the gsr sensor
const int GSR=A1;
int sensorValue=0;
int gsr_average = 0;
// PrintWriter output;

// this is for the pulse sensor
//  Variables
const int PulseWire = 0;       // PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED13 = 13;          // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;           // Determine which Signal to "count as a beat" and which to ignore.
                               // Use the "Gettting Started Project" to fine-tune Threshold Value beyond default setting.
                               // Otherwise leave the default "550" value.

PulseSensorPlayground pulseSensor;  // Creates an instance of the PulseSensorPlayground object called "pulseSensor"


void setup() {

  Serial.begin(9600);
// Configure the PulseSensor object, by assigning our variables to it. 
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       //auto-magically blink Arduino's LED with heartbeat.
  pulseSensor.setThreshold(Threshold);   

  // Double-check the "pulseSensor" object was created and "began" seeing a signal. 
   if (pulseSensor.begin()) {
    Serial.println("We created a pulseSensor Object !");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  }

}

void loop() {
  // this is gsr senso
  long sum = 0;
  for (int i=0; i < 10; i++) // average the 10 measurements using for loop

  {
    sensorValue = analogRead(GSR);
    sum += sensorValue;
    delay(5);
  }

  
  gsr_average = sum/10;
  Serial.print("gsr_average = ");
  Serial.println(gsr_average);
  int human_resistance = ((1024 + 2 * gsr_average) * 10000) / (516 - gsr_average); // following datasheet
  Serial.print("human_resistance = ");
  Serial.println(human_resistance);
  //delay(2000);

  // this is where the pulse sensor starts
  int myBPM = pulseSensor.getBeatsPerMinute();  // Calls function on our pulseSensor object that returns BPM as an "int".
                                               // "myBPM" hold this BPM value now.

  if (pulseSensor.sawStartOfBeat()) {            // Constantly test to see if "a beat happened". 
    Serial.println("♥  A HeartBeat Happened ! "); // If test is "true", print a message "a heartbeat happened".
    Serial.print("BPM: ");                        // Print phrase "BPM: " 
    Serial.println(myBPM);                        // Print the value inside of myBPM. 
    }

  delay(10);                    // considered best practice in a simple sketch. 
}
