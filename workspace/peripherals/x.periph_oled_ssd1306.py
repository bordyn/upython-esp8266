# connect SSD1306 with ESP8266 as follows
# 1. SDA to GPIO5 , SCL to GPIO4
# 2. 3.3V to 3.3V on ESP8266 (3V3)
# 3. GND to ground of the system.

from machine import Pin, I2C
import ssd1306 #save ssd1306.py in upython file system
from time import sleep

# ESP8266 Pin assignment
i2c_module = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# set oled properties
oled_width  = 128 #128 column pixel
oled_height = 32 #32 row pixel
oled = ssd1306.SSD1306_I2C(oled_width,oled_height,i2c_module)

# Try print hello world on 3 lines
oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
oled.show()

# now try some thing 
adc = machine.ADC(0)   # create an ADC object acting on a pin
val = adc.read_u16()     # read a raw analog value in the range 0-65535



while True:
    value = adc.read_u16()
    voltage = value/32768*3.3
    oled.fill(0)
    dis_str = 'volt : ' + "{:.3f}".format(voltage) + ' V'
    oled.text(dis_str, 0, 0)
    oled.show()
    sleep(0.1)
