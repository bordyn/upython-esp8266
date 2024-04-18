# Connect button switch as follows
# 1. connect one pin of button to port GPIO0 and 10k pull down resistor
# 2. connect the other pin to 3.3V

from time import sleep
from machine import Pin

# An example to track button status
# keep running these code and see the status
input_Pin = Pin(0, Pin.IN)
pin_value = input_Pin.value()
print ('Pin value is ' ,pin_value)

# Now we can see that 0 is inactive and 1 is inactive
# let's create a list that represent the status
status_list = ["released","pressed"]
pin_value = input_Pin.value()
print ('Pin value is ' ,status_list[pin_value])

# Now we bind a function into something
led2 = Pin(16, Pin.OUT)
last_pin_value = input_Pin.value()
while True:
    new_pin_value = input_Pin.value()
    if new_pin_value != last_pin_value:
        last_pin_value = new_pin_value
        print ("Pin Value is ",new_pin_value)
    led2.value(input_Pin.value() == 0)
    sleep(0.1)


    
    
    