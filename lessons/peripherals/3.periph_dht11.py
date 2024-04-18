# connect DHT11 kit as follows
#1. VCC connect to 3.3V
#2. Data - connect to GPIO14.
#          if ready made board that contains pull up resistor
#          ,then do nothing else connect pull up 10k resistor to Data
#3. GND connect to ground of the system.

from machine import Pin
import dht #build in module

# declare the sensor 
sensor = dht.DHT11(Pin(14))
sensor.measure() #then measure

# take measurement
temp = sensor.temperature()
hum = sensor.humidity()
print ('temperature is ',temp,' C')
print ('humidity is ',hum)

# some time the connection could be error
# keep exception handling would not crash program.
try:
    temp = sensor.temperature()
    hum = sensor.humidity()
    print ('temperature is ',temp,' C')
    print ('humidity is ',hum)
except Exception as e:
    print (e)
    print ('Fail to connect to DHT sensor')

# Assignment : displaying the temperature and humidity in display
# and log temperature and humidity to file every seconds for 1 minutes,
# when a button is pressed the whole report will be printed out for last 1 minute.