import network
from time import sleep

AccessPointName = "esp8266-ap" 

# config your network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=AccessPointName,password='123456789')

# wait for access point to active a bit
while ap.active() == False:
    sleep(0.1)

# connection successful
print('Access point',AccessPointName,'Connection successful')
print('Connect to this access point using ssid and password')

# wait a bit
while True:
    pass