import RPi.GPIO as GPIO
#import time as time


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(2,  GPIO.IN)

while True:
    if GPIO.input(2):
        GPIO.output(14, 1)
    else:
        GPIO.output(14, 0)
