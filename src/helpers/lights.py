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

    gpio_pins = [7, 11]

    set_warnings = bool(os.getenv('ENV').upper() == 'DEV')
    GPIO.setwarnings(set_warnings)

    GPIO.setmode(GPIO.BOARD)

    for pin in gpio_pins:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)

    while music.MUSIC_STATUS:
        if not music.MUSIC_STATUS:
            for pin in gpio_pins:
                GPIO.output(pin, GPIO.LOW)
