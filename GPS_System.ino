#include <SoftwareSerial.h>
#include <TinyGPS.h>

/* This code demonstrates the normal use of a TinyGPS object.
   It requires the use of SoftwareSerial, and we assume that  a
   4800-baud serial GPS device is hooked up on pins 4(rx) and 3(tx).
*/

TinyGPS gps;
SoftwareSerial ss(4, 3);

void setup()
{
  Serial.begin(115200);
  ss.begin(4800);
  
  Serial.print("Simple TinyGPS library v. "); Serial.println(TinyGPS::library_version());
  //Serial.println("by Manivel and team");
  Serial.println();
}

void loop()
{
  bool newData = false;
  unsigned long chars;
  unsigned short sentences, failed;

  // For one second we parse GPS data and report some key values
  for (unsigned long start = millis(); millis() - start < 1000;)
  {
    while (ss.available())
    {
      char c = ss.read();
      //Serial.write(c); // to see the GPS data flowing
      if (gps.encode(c)) // To check if a new valid sentence came in
        newData = true;
    }
  }

  if (newData)
  {
    float flat, flon; //latitude and longitude 
    unsigned long age; //a timestamp that tells us when the data was last updated.
    gps.f_get_position(&flat, &flon, &age);
    Serial.print("LAT=");
    Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
    Serial.print(" LON=");
    Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6);
    Serial.print(" SAT=");
    Serial.print(gps.satellites() == TinyGPS::GPS_INVALID_SATELLITES ? 0 : gps.satellites());
     
  }
  
  gps.stats(&chars, &sentences, &failed);
  Serial.print(" CHARS=");
  Serial.print(chars);
  Serial.print(" SENTENCES=");
  Serial.print(sentences);
  Serial.print(" CSUM ERR="); //checksum error for the Binary files that is loaded
  Serial.println(failed);
  if (chars == 0)
    Serial.println("** No characters received from GPS: check wiring **");
}
