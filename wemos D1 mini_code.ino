#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <EEPROM.h>
#include <PZEM004Tv30.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

const char *apSSID = "Hometer";
const char *apPassword = "myHometer";
ESP8266WebServer server(80);

String ssid = "";
String password = "";

const char* apiKey = "UQXBK7FAVI8H8Q8O";
const char* thingServer = "api.thingspeak.com";
PZEM004Tv30 pzem(D3, D4);

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "ntp.ku.ac.th", 7 * 3600); 
WiFiClient client; 

//int lastReset = 0;


void setup() {
  Serial.begin(115200);

  WiFi.softAP(apSSID, apPassword);

  // Serial.println("Access Point Started");
  // Serial.print("IP Address: ");
  // Serial.println(WiFi.softAPIP());

  server.on("/", HTTP_GET, [](void) {
    server.send(200, "text/html", getPage());
  });

  server.on("/config", HTTP_POST, []() {
    ssid = server.arg("ssid");
    password = server.arg("password");

    saveCredentialsToEEPROM();

    server.send(200, "text/plain", "เชื่อมต่ออุปกรณ์สำเร็จแล้ว");
    delay(1000);
    ESP.restart();
  });

  retrieveCredentialsFromEEPROM();

  server.begin();
  timeClient.begin();

}

void loop() {
  server.handleClient();
  if (ssid != "" && password != "") {
    WiFi.begin(ssid.c_str(), password.c_str());
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: " + WiFi.localIP().toString());
    ssid = "";
    password = "";
  }

  float voltage, current, power, energy;

  voltage = pzem.voltage();
  current = pzem.current();
  power = pzem.power();
  energy = pzem.energy();

  Serial.print("Voltage: ");
  Serial.println(voltage);
  Serial.print("Current: ");
  Serial.println(current);
  Serial.print("Power: ");
  Serial.println(power);
  Serial.print("Energy: ");
  Serial.println(energy);

  timeClient.update();
  unsigned long epochTime = timeClient.getEpochTime();

  // tmElements_t tm;
  // breakTime(epochTime, tm);
  // if (tm.Month != lastResetMonth) {
  //   energy = 0;
  //   lastResetMonth = tm.Month;
  // }

  String url = "/update?api_key=" + String(apiKey) +
               "&field1=" + String(voltage) +
               "&field2=" + String(current) +
               "&field3=" + String(power) +
               "&field4=" + String(energy) +
               "&created_at=" + String(epochTime);

  HTTPClient http;
  http.begin(client, thingServer, 80, url);
  int httpCode = http.GET();
  
  if (httpCode > 0) {
    Serial.println("Data sent to ThingSpeak successfully");
} else {
    Serial.print("Failed to send data to ThingSpeak. HTTP code: ");
    Serial.println(httpCode);
    Serial.print("Response: ");
    Serial.println(http.getString());
}

  http.end();
  
  delay(60000);
}

String getPage() {
  String page = "<html><body>";
  page += "<h1>ตั้งค่าอุปกรณ์</h1>";
  page += "<form action='/config' method='post'>";
  page += "WiFi SSID(ชื่อเครือข่ายWiFi): <input type='text' name='ssid' value='" + ssid + "'><br>";
  page += "WiFi Password(รหัสผ่านเครือข่ายWiFi): <input type='password' name='password' value='" + password + "'><br>";
  page += "<input type='submit' value='Submit'>";
  page += "</form></body></html>";
  return page;
}

void saveCredentialsToEEPROM() {
  EEPROM.begin(512);
  EEPROM.put(0, ssid);
  EEPROM.put(sizeof(ssid), password);
  EEPROM.commit();
  EEPROM.end();
}

void retrieveCredentialsFromEEPROM() {
  EEPROM.begin(512);
  EEPROM.get(0, ssid);
  EEPROM.get(sizeof(ssid), password);
  EEPROM.end();
}