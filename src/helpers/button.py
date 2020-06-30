"""
Button activator stuff.
"""

import RPi.GPIO as GPIO
from helpers import utilities
from helpers.utilities import LOGGER

LOGGER.debug('Button stuff!')

GPIO_PIN = 36
INPUT_VALUE = bool()

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

while True:
    INPUT_VALUE = GPIO.input(GPIO_PIN)

    if not INPUT_VALUE:
        LOGGER.debug(f'Button Pressed on pin {GPIO_PIN}.')

    while not INPUT_VALUE:
        INPUT_VALUE = GPIO.input(GPIO_PIN)
