import RPi.GPIO as GPIO
import     time as time


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

for i in range(10):
    GPIO.output(14, 1)
    time.sleep(0.5)
    
    GPIO.output(14, 0)
    time.sleep(0.5)
