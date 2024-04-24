# connect HD44780 with ESP8266 as follows
# 1. SDA to GPIO5 , SCL to GPIO4
# 2. 3.3V to 3.3V on ESP8266 (3V3)
# 3. GND to ground of the system.
# 4. copy lcd_api_i2c.py and lcd_api_i2c.py into esp8266 memory

"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from lcd_api_i2c import LcdApi_i2c

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

# 5. initiate I2C using I2C(scl=Pin(4), sda=Pin(5), freq=10000)
# 6. initiate lcd using LcdApi_i2c(i2c, DEFAULT_I2C_ADDR, 2, 16)
# 7. try putting string using lcd.putstr("It Works!\nSecond Line")

# 8. clear LCD using lcd.clear()
# 9. Turning backlight off, using lcd.backlight_off()
# 10. Turning backlight on, using lcd.backlight_on()
# 11. try printing some thing from the beginning ,using lcd.move_to(0, 0) and 
#     lcd.putstr("some string")

