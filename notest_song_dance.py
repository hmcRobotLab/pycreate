import unittest
import create
import song_dance

class TestSong_dance(unittest.TestCase):

    def test_look_around(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        song_dance.look_around(r, 5)
        r.shutdown()

    def test_c_chord(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        song_dance.c_chord(r, 5)
        r.shutdown()

    def test_dance(self):
        SERIAL_PORT = "/dev/ttyUSB0"
        r = create.Create(SERIAL_PORT)
        song_dance.dance(r, 2)
        r.shutdown()

if __name__ == '__main__':
    unittest.main()
