"""Movements for irobot create."""

import time
import create

SERIAL_PORT = "/dev/ttyUSB0"


def spin(r, num_repeats=2):
    """Spin in place.

    Keyword arguments:
    r -- robot object and serial connection.
    num_repeats -- number of clockwise and counter clockwise rotations.

    Returns: nothing, wheels move in opposite directions.

    """
    for i in range(num_repeats):
        r.go(0, 200)
        time.sleep(2)
        r.stop()
        time.sleep(.2)
        r.go(0, -200)
        time.sleep(2)
        r.stop()
        time.sleep(.2)


def shake(r, num_repeats=1):
    """Shake back and forth.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of forward and back motions.

    Returns: nothing, moves robot forward and backward.

    """
    for i in range(num_repeats):
        r.go(25)
        time.sleep(.1)
        r.stop()
        time.sleep(.1)
        r.go(-25)
        time.sleep(.1)
        r.stop()
        time.sleep(.1)


def side_step(r, num_repeats=1):
    """Step to the left and right side.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of steps left and right.

    Returns: nothing, moves robot from side to side.

    """
    for i in range(num_repeats):
        r.go(-10, -150)
        time.sleep(2)
        r.go(-20)
        time.sleep(1)
        r.go(-10, 150)
        time.sleep(2)
        r.stop()
        time.sleep(.15)
    for i in range(num_repeats):
        r.go(-10, 150)
        time.sleep(2)
        r.go(-20)
        time.sleep(1)
        r.go(-10, -150)
        time.sleep(2)
        r.stop()
        time.sleep(.15)
    for i in range(num_repeats):
        r.go(10, 150)
        time.sleep(2)
        r.go(20)
        time.sleep(1)
        r.go(10, -150)
        time.sleep(2)
        r.stop()
        time.sleep(.15)
    for i in range(num_repeats):
        r.go(10, -150)
        time.sleep(2)
        r.go(20)
        time.sleep(1)
        r.go(10, 150)
        time.sleep(2)
        r.stop()
        time.sleep(.15)


def twist(r, num_repeats=1):
    """Rotate back and forth.

    Keyword arguments:
    r -- robot object and serial connection.
    num_repeats -- number of rotations clockwise and counter clockwise.

    Returns: nothing, rotates robot CW and CCW.

    """
    for i in range(num_repeats):
        r.go(0, 50)
        time.sleep(.75)
        r.stop()
        time.sleep(.1)
        r.go(0, -50)
        time.sleep(.75)
        r.stop()
        time.sleep(.1)


def wiggle(r, num_repeats=2):
    """Move around in a small area.

    Keyword arguments:
    r -- robot object and serial connection
    num_repeats -- number of loops over moves sequence.

    Returns: nothing, moving forward and backwards, rotates left and right.

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
    spin(r)
    time.sleep(.25)
    shake(r)
    time.sleep(.25)
    side_step(r)
    time.sleep(.25)
    twist(r, 3)
    wiggle(r)
    r.shutdown()
