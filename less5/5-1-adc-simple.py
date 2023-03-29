import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


def adc():
    for value in range(levels):
        num2dac(value)
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return value


dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        val = adc()
        print(val, decimal2binary(val), " volts - {:.3}".format(val / levels * max_voltage))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()