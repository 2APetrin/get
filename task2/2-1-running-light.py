import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(leds, GPIO.OUT)

for x in range(3):
    for y in range(8):
        GPIO.output(leds[y], 1)
        time.sleep(0.2)
        GPIO.output(leds[y], 0)

GPIO.output(leds, 0)
GPIO.cleanup()