import network

# create access point using previous example
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

# now print out config
print(ap.ifconfig())

# save the simple_page.html to upython file system
# return html web page (text)
def web_page(sensor,page_file="temperature_page.html"):
    
    # measure temperature
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    with open(page_file,'r') as pf:
        html = pf.read()
    
    html = html.replace("{{temp1}}",str(temp))
    html = html.replace("{{temp2}}",str(hum))
    
    return html

# create a socket at port 80
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

from machine import Pin
import dht #build in module

# declare the sensor 
sensor = dht.DHT11(Pin(14))
sensor.measure() #them measure

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    
    print('Content = %s' % str(request))
    response = web_page(sensor)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
