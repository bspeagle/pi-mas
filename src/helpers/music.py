"""
Music module. FREEBIRD!!!!
"""

from pydub import AudioSegment
from pydub.playback import play
from helpers import utilities
from helpers.utilities import LOGGER

MUSIC_STATUS = bool()


def play_music():
    """
    Play some music.
    """

    global MUSIC_STATUS

    LOGGER.debug('STARTING!')

    MUSIC_STATUS = True

    song = AudioSegment.from_mp3('./audio/ticktock.wav')
    play(song - 5)

    MUSIC_STATUS = False

    LOGGER.debug('DONE!')
