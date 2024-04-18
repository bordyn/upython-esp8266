# connect mlx90614 kit as follows
#1. VCC connect to 3.3V
#2. SDA connect to GPIO4 of esp8266
#2. SCL connect to GPIO5 of esp8266
#3. GND connect to ground of the system.
# Note that the I2C lines can be connected to multiple devices.

# save mlx90614 to esp8266 internal file system
import mlx90614
from machine import I2C, Pin

# create i2c module , instantiation
i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = mlx90614.MLX90614(i2c)

# read amblient sensor using this module.
print(sensor.read_ambient_temp())
print(sensor.read_object_temp())
