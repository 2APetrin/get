import RPi.GPIO as GPIO


def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input()

        if num == 'q':
            break
        elif not is_number(num):
            print("Введено не число")
            continue

        num = int(num)

        if num < 0:
            print("Введено отрицательное значение")
            continue
        elif num > 255:
            print("Число вне диапозона")
            continue 

        print("Напряжение: {:.3}".format((num / 255) * max_voltage))
        print(decimal2binary(num))
        GPIO.output(dac, decimal2binary(num))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()