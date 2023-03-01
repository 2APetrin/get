import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

aux = [22, 23, 27, 18, 15, 14, 3, 2]
GPIO.setup(aux, GPIO.IN)

i = 0
while True:
    if (GPIO.input(aux[i])):
        GPIO.output(leds[i], 1)
    else:
        GPIO.output(leds[i], 0)
    i += 1

    if (i == 8):
        i = 0

GPIO.output(leds, 0)
GPIO.cleanup()