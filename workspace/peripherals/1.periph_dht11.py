# connect DHT11 kit as follows
# 1. VCC connect to 3.3V
# 2. Data - connect to GPIO14.
#           if ready made board that contains pull up resistor
#           ,then do nothing else connect pull up 10k resistor to Data
# 3. GND connect to ground of the system.

from machine import Pin
import dht #build in module

# 4. declare the sensor sensor = dht.DHT11(Pin(14))
# 5. measure using sensor.measure() #then measure

# 6. measure temp using sensor.temperature()
# 7. measure humidity using hum = sensor.humidity()

