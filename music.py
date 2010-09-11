"""Sounds for irobot create."""

import time
import create

SERIAL_PORT = "/dev/ttyUSB0"

def katamari():
    """Play Katamari and wait for it to finish."""
    r.playSong([(70,32),(72,16),(74,16),(75,16),(74,16),(70,16),(65,32),(68,32),(70,16),(68,16),(67,32),(65,32)])
    time.sleep(3)

def c_chord():
    """Play C chord and wait for it to finish."""
    for i in 'go':    
        r.playSong([(60,8),(64,8),(67,8),(72,8)])
        time.sleep(1)

def g_scale():
    """Play G scale and wait for it to finish."""
    for i in range(8,24,8):
        r.playSong([(55,i),(57,i),(59,i),(60,i),(62,i),(64,i),(66,i),(67,i),(67,i),(66,i),(64,i),(62,i),(60,i),(59,i),(57,i),(55,i)])
        time.sleep(2.25)

if __name__ == '__main__':
    r = create.Create(SERIAL_PORT)
    katamari()
    time.sleep(2)
    c_chord()
    time.sleep(1)
    g_scale()
    time.sleep(2)
    r.shutdown()
