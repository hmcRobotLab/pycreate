"""LED control for irobot create."""

import time
import create

SERIAL_PORT = "/dev/ttyUSB0"

def kitt_lights(r, num_repeats=4):
    """Imitate Knight Rider LEDs.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops of light sequence (default 4 times)

    Returns: nothing, changes light intensity and color.

    """
    for i in range(num_repeats):
        r.setLEDs(0, 255, 0, 0)
        time.sleep(.5)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.5)
        r.setLEDs(0, 0, 0, 1)
        time.sleep(.5)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.5)
        r.setLEDs(12, 255, 0, 0)
        time.sleep(.5)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.5)
        r.setLEDs(0, 0, 0, 1)
        time.sleep(.5)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.5)
        r.setLEDs(255, 255, 0, 0)
        time.sleep(.5)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.5)
        r.setLEDs(0, 0, 0, 1)
        time.sleep(.5)
        r.setLEDs(0, 0, 1, 0)
        time.sleep(.5)
        r.setLEDs(0, 255, 0, 0)

if __name__ == '__main__':
    r = create.Create(SERIAL_PORT)
    kitt_lights(r, 5)
    r.shutdown()
