"""Light (led) control for irobot create."""

import time
import create

SERIAL_PORT = "/dev/ttyUSB0"


def kitt(r, num_repeats=2):
    """Imitate Knight Rider LEDs.

    Keyword arguments:
    r -- robot object and serial connection.
    num_repeats -- number of loops of light sequence.

    Returns: nothing, changes light intensity and color.

    """
    for i in range(num_repeats):
        r.setLEDs(0, 255, 0, 0)
        time.sleep(.25)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.25)
        r.setLEDs(0, 0, 0, 1)
        time.sleep(.25)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.25)
        r.setLEDs(12, 255, 0, 0)
        time.sleep(.25)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.25)
        r.setLEDs(0, 0, 0, 1)
        time.sleep(.25)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.25)
        r.setLEDs(255, 255, 0, 0)
        time.sleep(.25)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.25)
        r.setLEDs(0, 0, 0, 1)
        time.sleep(.25)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.25)
        r.setLEDs(0, 255, 0, 0)


def look_around(r, num_repeats=2):
    """Imitate looking around with power, play, and advance leds.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops of light sequence.

    Returns: nothing, changes leds light intensity and color.

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
        for i in range(num_repeats):
            r.setLEDs(12, 255, 0, 0)
            time.sleep(.15)
            r.setLEDs(0, 0, 0, 0)
            time.sleep(.05)

if __name__ == '__main__':
    r = create.Create(SERIAL_PORT)
    kitt(r)
    look_around(r)
    r.shutdown()
