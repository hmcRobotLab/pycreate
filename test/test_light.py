import unittest
import create
import time
import light

class TestLight(unittest.TestCase):

    def test_kitt(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        light.kitt(r)
        r.shutdown()
    
    def test_look_around(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        light.look_around(r)
        r.shutdown()


if __name__ == '__main__':
    unittest.main()
