# Connect variable resistor 10k as follows
# 1. connect left pin of resistor to 10k resistor
# which connnect to 3.3V on the other side.
# 2. connect middle pin of resistor to ADC0
# 3. connect the right pin of resistor to ground.

from machine import ADC

# 3. simply read analog value, using ADC(0).read_u16()

# 4. convert analog value into internal voltage
# adc.read_u16()/65536*3.3

