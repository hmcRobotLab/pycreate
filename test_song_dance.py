import unittest
import create
import time
import leds

class TestSong_dance(unittest.TestCase):

    def test_look_around(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        leds.kitt_lights(r, 5)
        r.shutdown()

    def test_c_chord(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        leds.kitt_lights(r, 5)
        r.shutdown()

    def test_dance(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        leds.kitt_lights(r, 5)
        r.shutdown()

if __name__ == '__main__':
    unittest.main()
