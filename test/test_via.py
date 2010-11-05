import unittest
import create
import via

class TestVia(unittest.TestCase):


    def test_via(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        via.via(r, 2)
        r.shutdown()

if __name__ == '__main__':
    unittest.main()
