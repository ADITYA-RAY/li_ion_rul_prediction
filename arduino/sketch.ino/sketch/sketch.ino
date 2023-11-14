#define voltagePin A1
#define currentPin A0
#define temperaturePin A3
#define switchPin 12

float ref_voltage = 5;
bool charging = false;

 
void setup()
{
   pinMode(switchPin,OUTPUT);
   pinMode(2,OUTPUT);
   pinMode(3, OUTPUT);
   digitalWrite(2, HIGH);
   digitalWrite(3, HIGH);
   digitalWrite(12, HIGH);
   Serial.begin(9600);
}

double computeTemperature(){
   int adcData = analogRead(temperaturePin);
   float voltage = adcData* (4.8/1024);
   float temperature = (voltage)*100;
   return temperature;

}

float computeVoltage(){
  float R1 = 30000.0;
  float R2 = 7500.0; 
  float adc_voltage = 0.0;
  float in_voltage = 0.0;
  int adc_value = 0;
  adc_value = analogRead(voltagePin);
  adc_voltage  = (adc_value * 5) / 1024.0; 
  in_voltage = adc_voltage / (R2/(R1+R2)) ;
  return in_voltage;
}

float computeCurrent(){
  float current_adc = 0;
  float current_voltage = 0;
  float in_current = 0;
  current_adc = analogRead(currentPin);
  current_voltage  = (current_adc * ref_voltage*1000) / 1024.0; 
  in_current = (current_voltage-2500)*1000/100.00;  
  return in_current;

}

void switchControl(float voltage){
  if(charging && voltage > 3.60){
    digitalWrite(switchPin, HIGH);
    charging = false;
  }else if(!charging && voltage < 2.6){
    digitalWrite(switchPin, LOW);
    charging = true;
  }
}

void displayData(float voltage, float current, float temperature){

  Serial.print(voltage);
  Serial.print(", ");
  Serial.print((current + 100)/1000,2);
  Serial.print(", ");
  Serial.print(temperature);
  Serial.print(", ");
  Serial.println(charging);

  
}

void loop(){
  
  float voltage = 0;
  float current = 0;
  float temperature = 0;

  for(int i = 0; i < 200;i++){
    voltage += computeVoltage();
    current += computeCurrent();
    temperature += computeTemperature();
    delay(5);
  }
  
  voltage = voltage / 200;
  current /= -200;
  temperature /= 200;

   

  switchControl(voltage);
  displayData(voltage + 0.04,current,temperature);
    
  delay(2000);
}
