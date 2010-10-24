"""Light, song and motion control for irobot create."""

from create import Create
from light import look_around
from sound import c_chord
from move import spin, shake, twist

SERIAL_PORT = "/dev/ttyUSB0"

def dance(r, num_repeats=1):
    """First light up, then play a distinctive sound, continue with 
    a robot dance

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops to run

    Returns: nothing, changes lights, makes sound and moves.

    """
    for i in range(num_repeats):
        look_around(r)
        c_chord(r)
        spin(r)
        shake(r)
        twist(r)

if __name__ == '__main__':
    r = Create(SERIAL_PORT)
    dance(r)
    r.shutdown()
