"""
Main module. Duh.
"""

import asyncio
from helpers import lights, motor, music, utilities
from helpers.utilities import LOGGER


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


# do_thing_somewhere_else(music.play_music)

music.MUSIC_STATUS = True

do_thing_somewhere_else(lights.start_lights)
do_thing_somewhere_else(motor.run_motor)
