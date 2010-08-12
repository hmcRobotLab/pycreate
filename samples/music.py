import time
import create

SERIAL_PORT = "/dev/ttyUSB0"

r = create.Create( SERIAL_PORT )

x = 2

while x > 0:
    r.playSong( [(60,8),(64,8),(67,8),(72,8)] )
    time.sleep(1) # Give playSong time to finish
    x = x - 1

r.shutdown()
