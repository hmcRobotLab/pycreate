.. _03interactive:

Interactive Python
==================
.. sourcecode:: ipython

    $ ipython                # load the python interpreter into memory
    In [1]: import create    # load the create module into memory
    In [2]: r = create.Create('/dev/ttyUSB0')  # make serial connection, assign object to r
    In [3]: r.start()        # changes state from OFF_MODE to PASSIVE_MODE
    In [4]: r.toSafeMode()   # changes state from PASSIVE_MODE to SAFE_MODE
    In [5]: r.go( -5 )       # move at -5 cm/second, backwards
    In [6]: r.go( 0 )        # stops the create
    In [7]: r.go( 0, 10 )    # 0 cm/sec translational velocity and 10 deg/sec rotational
    In [8]: r.stop( )        # another way to stop, wrapper for go( 0 )
    In [9]: r.getSensor('ANGLE')  # reads the current value of angle sensor from robot
    Out[9]: 33               # and returns it
    In [10]: r.getSensor('DISTANCE') # reads the current value of distance sensor from robot
    Out[10]: 25              # and returns it
    In [11]: r.shutdown()    # stops and shuts down the connection to the robot
    In [12]: reset           # clears all namespaces from memory, clears software environment
