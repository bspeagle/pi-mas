"""
Test stuff.
"""

import asyncio
from time import sleep
from helpers import utilities
from helpers.utilities import LOGGER

THIS_THING = bool()


def a_task():
    """
    a func
    """

    global THIS_THING

    THIS_THING = True
    counter = 0
    while THIS_THING:
        counter += 1
        LOGGER.info(f'a func: {counter}')
        sleep(2)

    LOGGER.info('DONEDONEDONEDONEDONE!!!!!!!!!!!')


def b_task():
    """
    b func
    """

    counter = 0
    while True:
        counter += 1
        LOGGER.info(f'b func: {counter}')
        sleep(2)


def c_task():
    """
    c func
    """

    counter = 0
    while True:
        counter += 1
        LOGGER.info(f'c func: {counter}')
        sleep(2)


def background(function):
    """
    Asynchronous wrapper.
    """

    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, function, *args, **kwargs)

    return wrapped


@background
def do_thing_somewhere_else(app_method):
    """
    Function to run stuff in the background.
    """

    app_method()


def count_and_stuff_task():
    """
    bleh
    """

    global THIS_THING

    counter = 0
    while counter < 10:
        counter += 1
        sleep(4)

    THIS_THING = False


POSSIBLES = globals().copy()

for thing in POSSIBLES:
    if thing.endswith('_task'):
        method = POSSIBLES.get(thing)
        do_thing_somewhere_else(method)
