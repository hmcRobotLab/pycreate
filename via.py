"""Drive the robot through an environment via points stored in a file."""

from create import Create
from time import sleep

SERIAL_PORT = "/dev/ttyUSB0"


def load_numbers(r, filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        stripped_line = in_line.rstrip()
        print(stripped_line)
        turn_angle_in_deg, turn_velocity, fwd_distance, fwd_velocity = \
        [int(string) for string in stripped_line.split()]
        print(turn_angle_in_deg, turn_velocity, fwd_distance, fwd_velocity)
        r.go(0, turn_velocity) 
        r.waitAngle(turn_angle_in_deg)
        r.stop()
        sleep(.25)
        r.go(fwd_velocity)
        r.waitDistance(fwd_distance)
        r.stop()
        sleep(.25)
    in_file.close()


def via(r, filename):
    """Drive the robot according to data on each line in file.

    Keyword arguments:
    r -- robot object and serial connection
    filename -- data file with waypoints

    Returns: nothing, moves to points in filename.

    """
    pass
    #sense distance
    #waitAngle
    #waitDistance
    #sleep(long)
    #shutdown

if __name__ == '__main__':
    r = Create(SERIAL_PORT)
    filename = input("Please enter name of data file: ")
    load_numbers(r, filename)
    sleep(50)
    r.shutdown()
