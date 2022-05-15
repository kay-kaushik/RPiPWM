from gpiozero import DistanceSensor
from time import sleep
from gpiozero import PWMLED

led = PWMLED(17)

sensor = DistanceSensor(echo = 20, trigger = 21)
while True:
    dist = sensor.distance * 100
    print('Distance: ', dist)
    sleep(1)
    if dist < 30.0 and dist > 20.0:
        led.value  = 0.3
        sleep(1.0)
    elif dist < 20.0 and dist > 10.0:
        led.value = 0.6
        sleep(1.0)
    elif dist < 10.0:
        led.value = 1
        sleep(1.0)
    else:
        led.value = 0
        sleep(1.0)
