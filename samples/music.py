import sys
import time
import create

SERIAL_PORT = "/dev/ttyUSB0"

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
 
        for i in range(0, 10):
            r.playSong( [(60,8),(64,8),(67,8),(72,8)] )          
            time.sleep(0.02)

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
