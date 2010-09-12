"""Light, audio and motion control for irobot create."""

import time
import create

SERIAL_PORT = "/dev/ttyUSB0"

def look_around(r, num_repeats=10):
    """Imitate looking around.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops of light sequence (default 10 times)

    Returns: nothing, changes light intensity and color.

    """
    for i in range(num_repeats):
        r.setLEDs(0, 255, 0, 0)
        time.sleep(.05)
        r.setLEDs(0, 255, 1, 0)
        time.sleep(.05)
        r.setLEDs(0, 255, 1, 1)
        time.sleep(.05)
        r.setLEDs(0, 255, 1, 0)
        time.sleep(.05)
        r.setLEDs(0, 255, 0, 0)
        time.sleep(.05)
        r.setLEDs(12, 255, 0, 0)
        time.sleep(.25)

def c_chord(r, num_repeats=2):
    """Play C chord and wait for it to finish.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops of light sequence (default 2 times)

    Returns: nothing, produces notes

    """
    for i in range(num_repeats):
        r.playSong([(60,8),(64,8),(67,8),(72,8)])
        time.sleep(1)

def dance(r, num_repeats=2):
    """Move around in a small area.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops of light sequence (default 2 times)

    Returns: nothing, produces notes

    """
    for i in range(num_repeats):
        r.go(-10)
        time.sleep(.5)
        r.stop()
        r.go(10)
        time.sleep(.5)
        r.stop()
        for i in range(num_repeats):
            r.go(0, 30)
            time.sleep(2)
            r.stop()
            r.go(0, -30)
            time.sleep(2)
            r.stop()

if __name__ == '__main__':
    r = create.Create(SERIAL_PORT)
    look_around(r)
    c_chord(r)
    dance(r)
    r.shutdown()
