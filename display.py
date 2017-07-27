import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

SEGMENTS = [18,16,12,10,3,8,5,7]
NUMBERS = [19,15,13,11]
CHARS = {' ': (1,1,1,1,1,1,1,1),
         '0': (0,0,0,1,0,0,0,1)}

def init():
    for p in SEGMENTS:
        GPIO.setup(p, GPIO.OUT, initial=1)
    for p in NUMBERS:
        GPIO.setup(p, GPIO.OUT, initial=0)


def out_zip(pins, vals):
    for p, v in zip(pins, vals):
        GPIO.output(p, v)


def clear():
    for p in SEGMENTS:
        GPIO.output(p, 1)
    for p in NUMBERS:
        GPIO.output(p, 0)


def show(text, duration=1):
    for _ in range(0, duration * 50):
        number = 0
        for char in text[:4]:
            out_zip(SEGMENTS, CHARS.get(char, (1, 0, 0, 0, 0, 0, 0, 1)))
            GPIO.output(NUMBERS[number], 1)
            time.sleep(0.004)
            GPIO.output(NUMBERS[number], 0)
            number += 1
