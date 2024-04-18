from machine import Pin,I2C
from time import sleep

led_usr = Pin(16, Pin.OUT)
led_usr.value(1)

led = Pin(5, Pin.OUT)
led.value(0)

while True:
    led_usr.value(not led_usr.value())
    sleep(1.0)
