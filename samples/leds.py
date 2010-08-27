import create
import time

SERIAL_PORT = "/dev/ttyUSB0"
r = create.Create( SERIAL_PORT ) # create robot object

for i in [1,1,1,1]:
    r.setLEDs(0, 255, 0, 0) # powerColor, powerIntensity, play, advance
    time.sleep(.2)
    r.setLEDs(0, 255, i, 0)
    time.sleep(.2)
    r.setLEDs(0, 255, i, i)
    time.sleep(.2)
    r.setLEDs(0, 0, 0, 0)
    time.sleep(.2)

for i in 'four':
    for i in range(0, 256):
        r.setLEDs(0 + i, i, i, i)
        time.sleep(.005)
    for i in range(255, 0, -1):
        r.setLEDs(0 + i, i, i, i)
        time.sleep(.005)

r.shutdown()
