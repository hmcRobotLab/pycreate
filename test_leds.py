import unittest
import create
import time
import leds

class Testleds(unittest.TestCase):

    def test_kitt_lights(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        leds.kitt_lights(r, 5)
        r.shutdown()

if __name__ == '__main__':
    unittest.main()
