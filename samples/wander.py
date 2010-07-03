import sys
import time
import random
import create 

SERIAL_PORT = "/dev/ttyUSB0"

# our states
GO_STATE = 1;
TURN_STATE = 2;
SSTRINGS = [ "NONE (0)", "GO_STATE (1)", "TURN_STATE (2)" ]
STATE = GO_STATE

def shutdown( r ):
    """ stop robot and close serial port """
    r.drive( (0,0) )   # stops
    time.sleep(0.5)
    r.shutdown()       # closes port
    time.sleep(0.5)

def transition( destinationState ):
    """ state changer """
    global STATE
    print " Leaving state: ", SSTRINGS[STATE]
    print "Entering state: ", SSTRINGS[destinationState]
    STATE = destinationState

if __name__ == "__main__":

    r = create.Create( SERIAL_PORT )
    settime = time.time()

    resp = raw_input("Ready to roll? ")
    if resp[0] != 'y':
        shutdown(r)

    # sense - plan - act loop
    try:

        while True:

            # sensing
            print "Sensing..."
            r.sense()
            thistime = time.time()

            print "bump status:"
            print "  left: ", r.bump_left
            print " right: ", r.bump_right
            print

            print "Planning..."
           if STATE == GO_STATE and (r.bump_left or r.bump_right):
                transition( TURN_STATE )
                r.stop()
                desiredtime = random.uniform(1,3) # 1-3 seconds of turn
                settime = time.time()

            if STATE == TURN_STATE and (thistime - settime > desiredtime):
                transition( GO_STATE )

            print "Acting..."

            if STATE == GO_STATE:
                r.drive( (50,50) )

            if STATE == TURN_STATE:
                r.drive( (-50,50) )
                time.sleep( 0.25 )  # extra waiting

        # clean up!
        shutdown( r )
        time.sleep(0.5)
        print "quitting..."
        sys.exit()

    # any errors?
    except:
        print "Unexpected error caught - shutting down."
        shutdown( r )
        print "Shutdown complete."
        time.sleep(0.5);
        raise   # re-establishing the exception...
        # raising the exception will make the shell print out
        # error and the line number - important for debugging!
