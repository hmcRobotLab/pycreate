import unittest
import create
import time
import sense

SERIAL_PORT = "/dev/ttyUSB0"

class TestSense(unittest.TestCase):

    def test_main(self):
        r = create.Create(SERIAL_PORT)
        sense.main(r)
        r.shutdown()
    
if __name__ == '__main__':
    unittest.main()
