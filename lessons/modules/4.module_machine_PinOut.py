from time import sleep
from machine import Pin

# turning LED on board
led1 = Pin(2, Pin.OUT)
led1.value(0)
sleep(1.0)
led1.value(1)

# turning LED on board 2
led2 = Pin(16, Pin.OUT)
led2.value(0)
sleep(1.0)
led2.value(1)

# it's time to do some fancy pattern
def blink_led_on_board(led,sleep_period=0.25):
    led.value(0)
    sleep(sleep_period)
    led.value(1)
    sleep(sleep_period)

incremental_pattern = [(i+1)*2 for i in range(0,4)]
print (incremental_pattern)
for pattern in incremental_pattern:
    for i in range(0,pattern):
        blink_led_on_board(led2)
    sleep(2)

# this means forever
pattern_idx = 0
while True:
    pattern = incremental_pattern[pattern_idx]
    for i in range(0,pattern):
        blink_led_on_board(led2)
    sleep(2)
    pattern_idx = pattern_idx + 1
    if pattern_idx >= len(incremental_pattern):
        pattern_idx = 0
    
# Assignment : try your SOS pattern forever loop
# . . . ___ ___ ___ . . .
    
    
    