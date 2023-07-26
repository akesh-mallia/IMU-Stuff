import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

i2c = board.I2C()
sensor = LSM6DSOX(i2c)

counter = 0

with open("IMU_Data.txt", "a") as f:
    while counter <= 20:
        acc = ("Acceleration: X: %.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
        gyro = ("Gyro: X: %.2f, Y: %.2f, Z: %.2f radians/s" %(sensor.gyro))
        f.write(gyro)
        f.write("\n")
        f.write(acc)
        f.write("\n")
        counter += 1 
        print(counter)
        time.sleep(0.5)
