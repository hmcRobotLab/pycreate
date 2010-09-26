import unittest
import create
import time
import sound

SERIAL_PORT = "/dev/ttyUSB0"

class TestSounds(unittest.TestCase):

    def test_katamari(self):
        r = create.Create(SERIAL_PORT)
        sound.katamari(r)
        time.sleep(2)
        r.shutdown()

    def test_c_chord(self):
        r = create.Create(SERIAL_PORT)
        sound.c_chord(r)
        time.sleep(2)
        r.shutdown()

    def test_g_scale(self):
        r = create.Create(SERIAL_PORT)
        sound.g_scale(r)
        time.sleep(2)
        r.shutdown()

if __name__ == '__main__':
    unittest.main()
