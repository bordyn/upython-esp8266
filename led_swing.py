from machine import Pin,I2C
from time import sleep

led = Pin(2, Pin.OUT)
led.value(0)

while True:
    print (":led value is" + str(led.value()))
    led.value(not led.value())
    sleep(1.0)
