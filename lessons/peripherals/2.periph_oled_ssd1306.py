# connect SSD1306 with ESP8266 as follows
# 1. SDA to GPIO5 , SCL to GPIO4
# 2. 3.3V to 3.3V on ESP8266 (3V3)
# 3. GND to ground of the system.

# Connect variable resistor 10k as follows
# 1. connect left pin of resistor to 10k resistor
# which connnect to 3.3V on the other side.
# 2. connect middle pin of resistor to ADC0
# 3. connect the right pin of resistor to ground.

from machine import Pin, I2C
import ssd1306 #save ssd1306.py in upython file system
from time import sleep

# ESP8266 Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# set oled properties
oled_width  = 128 #128 column pixel
oled_height = 32 #32 row pixel
oled = ssd1306.SSD1306_I2C(oled_width,oled_height,i2c)

# init ADC property
adc = machine.ADC(0)   # create an ADC object acting on a pin

# pervious code on ADC scale
scale_min = 0
scale_max = 65536/2
def adc_value_to_scale(val,min_scale=scale_min,max_scale=scale_max):
    return  val/(max_scale-min_scale)*100

while True:
    scale = adc_value_to_scale(adc.read_u16())
    oled.fill(0) # special routine to remove previous display
    dis_str = 'Volume : ' + "{:.1f}".format(scale) + ' %'
    oled.text(dis_str, 0, 0)
    oled.show()
    sleep(0.1)