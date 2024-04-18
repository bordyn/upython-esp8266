# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep

adc = machine.ADC(0)   # create an ADC object acting on a pin
val = adc.read_u16()     # read a raw analog value in the range 0-65535

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#oled.text('Hello, World 1!', 0, 0)
#oled.text('Hello, World 2!', 0, 10)
#oled.text('Hello, World 3!', 0, 20)
        
oled.show()

while True:
    value = adc.read_u16()
    voltage = value/32768*3.3
    oled.fill(0)
    dis_str = 'volt : ' + "{:.3f}".format(voltage) + ' V'
    oled.text(dis_str, 0, 0)
    oled.show()
    sleep(0.1)