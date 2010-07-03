.. _03interactive:

==================
Interactive Python
==================

Getting started with ipython::

    $ ipython           # Loads the python interpreter into memory
    import create       # Loads the create module into memory
    r = create.Create('/dev/ttyUSB0')    # Make serial connection, assign object to r
    r.start()           # changes state from OFF_MODE to PASSIVE_MODE
    r.toSafeMode()      # changes state from PASSIVE_MODE to SAFE_MODE
    r.go( -5 )          # go at -5 cm/second, backwards
    r.go( 0 )           # stops the create
    r.go( 0, 10 )       # 0 cm/sec translational velocity and 10 deg/sec rotational
    r.stop( )           # another way to stop, same as r.go( 0 )
    r.getSensor('ANGLE') # Reads the value of angle sensor from robot and returns it
    r.getSensor('DISTANCE') # Reads the value of distance sensor from robot and returns it
    r.shutdown()        # shuts down the connection to the Create, after first
                        # stopping the Create and putting the Create into passive mode
    reset               # clears all namespaces from memory, clears software environment

Then push the power button to turn off the power to the robot.
Then return robot to charger, should see the blinking amber charging led.
