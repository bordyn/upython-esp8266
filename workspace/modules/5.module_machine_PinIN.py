# Connect button switch as follows
# 1. connect one pin of button to port GPIO0 and 10k pull down resistor
# 2. connect the other pin to 3.3V

from time import sleep
from machine import Pin

# An example to track button status
# keep running these code and see the status
# 3. Reading Pin 0 using Pin(0, Pin.IN).value()  
input_Pin = Pin(0, Pin.IN)

# Now we can see that 0 is inactive and 1 is inactive
# let's create a list that represent the status
# 4. map the value to status_list
status_list = ["released","pressed"]



    
    
    