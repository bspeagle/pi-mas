"""
Main module. Duh.
"""

from time import sleep
import RPi.GPIO as GPIO
from helpers import utilities
from helpers.utilities import LOGGER

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(10, GPIO.HIGH)
    sleep(1)
    GPIO.output(10, GPIO.LOW)
    sleep(1)
