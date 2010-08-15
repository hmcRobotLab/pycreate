What is Create
==============
iRobot `Create <http://www.irobot.com/create/>`_ is a mobile robot platform.  Create is preassembled and ready to use.  iRobot provides a documented open serial interface called, "iRobot Create Open Interface."  Pycreate uses a Python implementation of this interface from `Rose-Hulman <http://en.wikipedia.org/wiki/Rose%E2%80%93Hulman_Institute_of_Technology>`_.

Requirements

* Python >= 3.0::

    $ sudo apt-get install python3.1

* PySerial >= 1.0::
    
    $ wget http://pypi.python.org/packages/source/p/pyserial/pyserial-2.5.tar.gz#md5=34340820710239bea2ceca7f43ef8cab
    $ tar zxvf pyserial-2.5.tar.gz
    $ cd pyserial-2.5/
    $ sudo python3.1 setup.py install

Resouces

* http://www.rose-hulman.edu/class/csse/resources/Robotics/

Hardware
========

Choose any of these four options to get started:

#. Teather: Create and computer directly connected with wire. (serial 9pin to usb or rs232)
#. Teather and wireless: Above setup with an additional computer and 802.11 network
#. Wireless: Create and computer wireless connection via bluetooth network
#. Simulator: Computer with create software environment and without the create hardware

After choosing an above option, its time to get started (see Resources for Simulator):

* Power up robot on floor and verify green led
* Make physical and/or wireless connection between robot and computer
* Determine serial port name used to connect to robot::

    $ ls /dev/tty <tab>  # python needs this variable to open the serial connection
    /dev/ttyUSB0         # my serial port name associated with create, yours may differ

* Open serial port for communication between robot and computer with create.py module (see below).

Software
========
Setup environment by setting appropriate PYTHONPATH, cloning the latest pycreate software to your computer, and starting python3.1::

    $ echo "export PYTHONPATH=/home/mgobryan/pycreate" >> ~/.bashrc
    $ source ~/.bashrc
    $ cd ~
    $ git clone git://github.com/mgobryan/pycreate
    $ python3.1
    >>> import create    # load the create module into memory
    >>> r = create.Create('/dev/ttyUSB0')  # open serial connection, assign object to r

Move::

    >>> r.go( -5 )       # move at -5 cm/second, backwards
    >>> r.stop()         # stops the create
    >>> r.go( 0, 10 )    # 0 cm/sec translational velocity and 10 deg/sec rotational
    >>> r.stop( )        # stops the create

Sense::

    >>> r.getSensor('ANGLE')  # reads the current value of angle sensor from robot
    107                  # and returns it
    >>> r.getSensor('DISTANCE') # reads the current value of distance sensor from robot
    -271                 # and returns it

Light::

    >>> r.setLEDs(0, 255, 1, 1)   # Green, Bright, Green, Green
    >>> r.setLEDs(255, 255, 0, 0) # Red, Bright, Off, Off

Demo::

    >>> r.demo(0)        # starts wander demo, other demos 1 - 9
    >>> r.demo()         # stops demo

Music::

    >>> r.playSong( [(60,8),(64,8),(67,8),(72,8)] )
    >>> r.shutdown()     # stops, then closes the connection to the robot
    >>> <CTRL> d         # closes interactive python interpreter

Appendix
========


