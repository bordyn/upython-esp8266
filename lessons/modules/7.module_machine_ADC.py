# Connect variable resistor 10k as follows
# 1. connect left pin of resistor to 10k resistor
# which connnect to 3.3V on the other side.
# 2. connect middle pin of resistor to ADC0
# 3. connect the right pin of resistor to ground.

from machine import ADC

# simply read analog value
adc = ADC(0)   # create an ADC object acting on a pin ADC0 (A0)
val = adc.read_u16()     # read a raw analog value in the range 0-65535
print (val)

# convert analog value into internal voltage
print ('voltage is ',adc.read_u16()/65536*3.3,' Volt')

# convert this into desirable scale
scale_min = 0
scale_max = 65536/2
def adc_value_to_scale(val,min_scale=scale_min,max_scale=scale_max):
    return  val/(max_scale-min_scale)*100

# simply turn the variable resistor and keep running below 
print ('scale value is ',adc_value_to_scale(adc.read_u16()))
