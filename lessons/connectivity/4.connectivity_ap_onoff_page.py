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
def web_page(led,page_file="onoff_page.html"):
    if led.value() == 0:
        gpio_state="ON"
    else:
        gpio_state="OFF"
    with open(page_file,'r') as pf:
        html = pf.read()
    html = html.replace("{{gpio_state}}",gpio_state)
    return html

# create a socket at port 80
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

from machine import Pin
# turning LED on board 2
led2 = Pin(16, Pin.OUT)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    led_cmd_on = request.find(b'/?led=on')
    led_cmd_off = request.find(b'/?led=off')
    if led_cmd_on > 0 and led_cmd_on < 256:
        print('LED ON')
        led2.value(0)
    elif led_cmd_off > 0 and led_cmd_off < 256:
        print('LED OFF')
        led2.value(1)
    response = web_page(led2)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()

