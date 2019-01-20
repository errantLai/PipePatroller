#include <SoftwareSerial.h>
#define RX 10
#define TX 11
String AP = "Electral";       
String PASS = "warofmagic";
String HOST = "35.211.247.147";
String PORT = "3002";
String API = "78";

int countTrueCommand;
int countTimeCommand; 
boolean found = false; 
int valSensor = 1;
SoftwareSerial esp8266(RX,TX); 

#include <dht.h>
#include <Si7021.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>


dht DHT;
#define DHT11_PIN 7
Si7021 si7021;
Adafruit_BMP280 bme; 
 
  
void setup() {
  Serial.begin(9600);
  esp8266.begin(115200);
  sendCommand("AT",5,"OK");
  sendCommand("AT+CWMODE=1",5,"OK");
  sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK");
  uint64_t serialNumber = 0ULL;
  si7021.begin();
  serialNumber = si7021.getSerialNumber();
}
void loop() {
 String udist = "-999"; 
 String bc = String (random (200) + 1970); 
 int chk = DHT.read11(DHT11_PIN);
 double sm = si7021.measureHumidity();
 double smt = si7021.getTemperatureFromPreviousHumidityMeasurement(); 
 double dht = DHT.temperature; 
 double e = bme.readPressure(); 
 String getData = "GET /input?a=990&b=" + String(sm) + "&c=" + smt + "&d=" + dht + "&e=" + e;
 delay(5000); 
sendCommand("AT+CIPMUX=1",5,"OK");
 sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
 sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
 esp8266.println(getData);delay(1500);countTrueCommand++;
 sendCommand("AT+CIPCLOSE=0",5,"OK");
Serial.println(getData);

}
int getSensorData(){
  return random(1000); // Replace with 
}
void sendCommand(String command, int maxTime, char readReplay[]) {
  Serial.print(countTrueCommand);
  Serial.print(". at command => ");
  Serial.print(command);
  Serial.print(" ");
  while(countTimeCommand < (maxTime*1))
  {
    esp8266.println(command);//at+cipsend
    if(esp8266.find(readReplay))//ok
    //delay(5000); 
    {
      found = true;
      break;
    }
  
    countTimeCommand++;
  }
  
  if(found == true)
  {
    Serial.println("Victory");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(found == false)
  {
    Serial.println("Fail");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
 }
