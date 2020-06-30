"""
LED diode stuff.
"""

import os
import RPi.GPIO as GPIO
from helpers import music, utilities
from helpers.utilities import LOGGER


def start_lights():
    """
    Turn the lights on!
    """

    gpio_pin = 7

    set_warnings = bool(os.getenv('ENV').upper() == 'DEV')
    GPIO.setwarnings(set_warnings)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_pin, GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(gpio_pin, GPIO.HIGH)

    while music.MUSIC_STATUS:
        if not music.MUSIC_STATUS:
            GPIO.output(gpio_pin, GPIO.LOW)
