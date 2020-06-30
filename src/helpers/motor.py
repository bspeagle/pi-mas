"""
Stepper motor stuff.
"""

import time
import RPi.GPIO as GPIO
from helpers import music, utilities
from helpers.utilities import LOGGER


def run_motor():
    """
    Do motor stuff.
    """

    GPIO.setmode(GPIO.BOARD)

    control_pins = [18, 22, 24, 26]

    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    halfstep_seq = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
    ]

    while music.MUSIC_STATUS:
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

    GPIO.cleanup()
