import unittest
import create
import time
import move

SERIAL_PORT = "/dev/ttyUSB0"

class TestMoves(unittest.TestCase):

    def test_spin(self):
        r = create.Create(SERIAL_PORT)
        move.spin(r)
        time.sleep(2)
        r.shutdown()

    def test_shake(self):
        r = create.Create(SERIAL_PORT)
        move.shake(r)
        time.sleep(2)
        r.shutdown()

    def test_side_step(self):
        r = create.Create(SERIAL_PORT)
        move.side_step(r)
        time.sleep(2)
        r.shutdown()

    def test_twist(self):
        r = create.Create(SERIAL_PORT)
        move.twist(r)
        time.sleep(2)
        r.shutdown()

    def test_wiggle(self):
        r = create.Create(SERIAL_PORT)
        move.wiggle(r)
        time.sleep(2)
        r.shutdown()

if __name__ == '__main__':
    unittest.main()
