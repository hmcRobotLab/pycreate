"""Sounds for irobot create."""

import time
import create

SERIAL_PORT = "/dev/ttyUSB0"


def katamari(r, num_repeats=1):
    """Play Katamari and wait for it to finish.

    Keyword arguments:
    r -- robot object and serial connection.
    num_repeats -- number of loops of sound sequence.

    Returns: nothing, produces sound.

    """
    for i in range(num_repeats):
        r.playSong([(70, 32), (72, 16), (74, 16), (75, 16), (74, 16), \
                    (70, 16), (65, 32), (68, 32), (70, 16), (68, 16), \
                    (67, 32), (65, 32)])
        time.sleep(3)


def c_chord(r, num_repeats=1):
    """Play C chord and wait for it to finish.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops of sound sequence.

    Returns: nothing, produces sound.

    """
    for i in range(num_repeats):
        r.playSong([(60, 8), (64, 8), (67, 8), (72, 8)])
        time.sleep(.75)


def g_scale(r, num_repeats=1):
    """Play G scale and wait for it to finish.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops of sound sequence.

    Returns: nothing, produces sound.

    """
    for i in range(num_repeats):
        for i in range(8, 16, 8):
            r.playSong([(55, i), (57, i), (59, i), (60, i), (62, i), (64, i), \
                        (66, i), (67, i), (67, i), (66, i), (64, i), (62, i), \
                        (60, i), (59, i), (57, i), (55, i)])
            time.sleep(2)

if __name__ == '__main__':
    r = create.Create(SERIAL_PORT)
    katamari(r)
    time.sleep(2)
    c_chord(r)
    time.sleep(1)
    g_scale(r)
    time.sleep(2)
    r.demo(8)
    time.sleep(1)
    r.shutdown()
