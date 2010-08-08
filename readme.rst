.. contents:: Table of Contents

**Pycreate uses a Python implementation of the iRobot Create Open Interface to complete tasks.**

Requirements
============
* Python >= 3.0::

    $ sudo apt-get install python3.1

* PySerial >= 1.0::
    
    $ wget http://pypi.python.org/packages/source/p/pyserial/pyserial-2.5.tar.gz#md5=34340820710239bea2ceca7f43ef8cab
    $ tar zxvf pyserial-2.5.tar.gz
    $ cd pyserial-2.5/
    $ sudo python3.1 setup.py install

What is Create
==============
iRobot `Create <http://www.irobot.com/create/>`_ is a mobile robot platform.

Why use Create
==============
Create is preassembled and ready to use.  iRobot provides a documented open serial interface called, "iRobot Create Open Interface."

Resouces
========
* http://www.rose-hulman.edu/class/csse/resources/Robotics/
* http://roboticsprimer.sourceforge.net/workbook/Main_Page

Hardware choices
================
#. Teather: Create and computer directly connected with wire. (serial 9pin to usb or rs232) 
#. Teather and wireless: Above setup with an additional computer and 802.11 network
#. Wireless: Create and computer wireless connection via bluetooth network
#. Simulator: Computer with create software environment and without the create hardware

Connect
=======
* Start with robot on open floor space
* Press power button on robot, verify green led
* Start robot laptop, if necessary configure wireless and sshd
* Connect usb to serial cable between robot and laptop (if necessary)
* Secure robot and robot laptop together with velcro (if necessary)
* Start base laptop, and wireless, then ssh to robot laptop (if necessary)::

    $ ssh -Y from base laptop to access robot laptop.

* On robot laptop, lookup serial port name connected to robot.  Python needs this variable to make the serial connection::

    $ ls /dev/tty <tab>
    /dev/ttyUSB0         # is my connection, yours may differ

Software
========
Clone the latest software to your computer::

    $ git clone git://github.com/mgobryan/pycreate

Change into the directory with create.py::

    $ cd pycreate

Start Python (load the python interpreter into memory)::    

    $ python

    >>> import create    # load the create module into memory
    >>> r = create.Create('/dev/ttyUSB0')  # make serial connection, assign object to r
    >>> r.go( -5 )       # move at -5 cm/second, backwards
    >>> r.go( 0 )        # stops the create
    >>> r.go( 0, 10 )    # 0 cm/sec translational velocity and 10 deg/sec rotational
    >>> r.stop( )        # another way to stop, wrapper for go( 0 )
    >>> r.getSensor('ANGLE')  # reads the current value of angle sensor from robot
    107                  # and returns it
    >>> r.getSensor('DISTANCE') # reads the current value of distance sensor from robot
    -271                 # and returns it
    >>> r.shutdown()     # stops, then closes the connection to the robot
