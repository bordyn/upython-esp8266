# Connect button switch as follows
# 1. connect one pin of button to port GPIO0 and 10k pull down resistor
# 2. connect the other pin to 3.3V

from time import sleep
from machine import Pin

# let's define a function to output led
led2 = Pin(16, Pin.OUT)
def led_onoff(val):
    led2.value(val==0)

# define Pin 0 as interrupt (IRQ)
irq_Pin = Pin(0, Pin.IN,Pin.PULL_UP)

# lambda function is anonymous in line that allows you to input any argument
# For instance, this example take v as input to function led_onoff
# where v represents irq_Pin.value()
irq_Pin.irq(lambda val : led_onoff(val=irq_Pin.value()))

# interrupts allow you to do any thing in forever loop without monitoring.
while True:
    pass