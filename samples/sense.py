import sys
import time
import create

SERIAL_PORT = "/dev/ttyUSB0"
SLIST = ["WALL","CLIFF_LEFT","CLIFF_RIGHT","DISTANCE","ANGLE"]

def shutdown( r ):
    """ stop robot and close serial port """
    r.drive( (0,0) )   # stops
    time.sleep(0.5)
    r.shutdown()       # closes port
    time.sleep(0.5)

if __name__ == "__main__":

    r = create.Create( SERIAL_PORT )
    r.start()
    r.toSafeMode()
    
    try:
 
        for i in SLIST:
            data = r.getSensor(i)
            print i, "=", data

        shutdown( r )
        time.sleep(0.5)
        print "quitting..."
        sys.exit()

    except:
        print "Unexpected error caught - shutting down."
        shutdown( r )
        print "Shutdown complete."
        time.sleep(0.5);
        raise   # re-establishing the exception...
        # raising the exception will make the shell print out
        # error and the line number - important for debugging!
