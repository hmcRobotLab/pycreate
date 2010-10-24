What is Create
--------------
iRobot `Create <http://www.irobot.com/create/>`_ is a mobile robot platform 
that is preassembled and ready to use.  iRobot provides a documented open 
serial interface called, "iRobot Create Open Interface."  Pycreate uses a 
Python implementation of this interface from 
`Rose-Hulman <http://www.rose-hulman.edu/class/csse/resources/>`_.

Requirements

* Python >= 3.1::

    $ sudo apt-get install python3.1

* PySerial >= 1.0::
    
    $ wget http://pypi.python.org/packages/source/p/pyserial/pyserial-2.5.tar.gz#md5=34340820710239bea2ceca7f43ef8cab
    $ tar zxvf pyserial-2.5.tar.gz
    $ cd pyserial-2.5/
    $ sudo python3.1 setup.py install

* TkInter::

    $ sudo apt-get install python3.1-tk

Resouces

* http://www.rose-hulman.edu/class/csse/csse120/201110robotics/
* http://www.rose-hulman.edu/class/csse/resources/Robotics/
* http://mcsp.wartburg.edu/zelle/python/

Hardware
--------

Choose any of these four options to get started:

#. Teather: Create and computer directly connected with wire. (serial 9pin to usb or rs232)
#. Teather and wireless: Above setup with an additional computer and 802.11 network
#. Wireless: Create and computer wireless connection via bluetooth network
#. Simulator: Computer with create software environment and without the create hardware

After choosing an above option, get started (see Resources for Simulator):

#. Power up robot on floor and verify green led
#. Make physical and/or wireless connection between robot and computer
#. Determine serial port name used to connect to robot
#. Open serial port between robot and computer with python

Software
--------
Set appropriate PYTHONPATH, clone pycreate to your home directory, and start python3.1::

    $ echo "export PYTHONPATH=/home/mgobryan/pycreate" >> ~/.bashrc
    $ source ~/.bashrc
    $ cd ~
    $ git clone git://github.com/mgobryan/pycreate
    
    Python needs the OS assigned serial port name given to robot hardware.
    $ ls /dev/tty <tab>  # determine the correct serial port to robot hardware
    /dev/ttyUSB0         # my serial port name associated with create, yours may differ
    
    $ python3.1          # start python
    >>> import create    # load the create module into memory
    >>> r = create.Create('/dev/ttyUSB0')  # open serial connection, assign object to r

Sense::

    >>> r.getSensor('ANGLE')  # read the current value of angle sensor from robot
    107
    >>> r.getSensor('DISTANCE') # read the current value of distance sensor from robot
    -271

Light::

    >>> r.setLEDs(0, 255, 1, 1)   # Green, Bright, Green, Green
    >>> r.setLEDs(255, 255, 0, 0) # Red, Bright, Off, Off

Music::

    >>> r.playSong( [(60,8),(64,8),(67,8),(72,8)] ) # a C chord

Move::

    >>> r.go(-5)         # move at -5 cm/second, backwards
    >>> r.stop()         # stop robot motion
    >>> r.go(0, 10)      # 0 cm/sec translational velocity and 10 deg/sec rotational
    >>> r.shutdown()     # stop and close the connection to the robot

Graphic::

    >>> import graphics  # load the graphics module into memory
    >>> win = graphics.GraphWin("Me", 100, 100) # open a 100x100 window
    >>> win.close()      # close window
    >>> <CTRL> d         # close python

Appendix
--------

* sense.py:

  - a function to gather sensors key, value pairs.  Open a file and write the 
    sensor data to the file and stdout one sensor data point per line.

* light.py:

  - Includes a function kitt() that takes two parameters: the robot and 
    num_repeats.  Toggles the play and advance lights on/off in sequence 
    repeated num_repeats times and has a different color on the power led.

* dance.py:

  - Includes a function dance().  First light up, then play a distinctive 
    sound, continue with a robot dance, finally repeat zero or more times. 

* via.py:

  - Drive the robot through an environment via points stored in a file.  Use 
    feedback from the encoders to drive a certain distance.  An encoder is a 
    mechanical device attached the robot's wheels to measure how far it has 
    traveled.  
        
        * Prompt the user for the file name and open the file with that name.   
        * Read each line of the file. Each line will contain 4 values:
          turn_angle_in_deg, turn_speed, fwd_distance_in_cm, fwd_velocity.  
        * For each line, turn robot based upon the turn angle and speed, then 
          drive the robot forward based upon the forward distance and velocity. 

* wander.py:
 
  - Includes a function wander() that takes three parameters: the robot, and 
    linear and angular velocity.  The parameters should be in the following 
    order:

        1. robot
        2. [optional] Linear Velocity in cm/s, default = 15
        3. [optional] Angular Velocity in deg/s, default = 20

  - Select a random angle between or including -180 and 180 degrees (via 
    randrange), turn the robot that much, select a random distance between 10 
    and 30 cm, and move the robot forward that much. Be sure that the sign on 
    your velocities and distances are the same. Also make sure that when you 
    calculate how long to sleep, you allow the answer to be a float. Repeat 
    this random sequence of turn+drive 5 times or until its cliff sensor is 
    triggered (i.e. pick it up) and use the go() method.

* smart_wander.py:

  - smart_wander() should cause the robot to wander around randomly (turn then 
    move, repeated 5 times), as it did for wander(), but also move away from 
    any obstacles into which it bumps. Specifically: 
       
        1. move for random angles between -180 and 180 degrees, and distances 
        between 10 and 30 cm. Reminder: be sure that the sign on your 
        velocities and distances are the same. Also, do NOT use wait_Angle() 
        or wait_Distance() (or turnTo() or moveTo() which use them), since they 
        monopolize the serial port, which you need for sensor data. Therefore, 
        you will have to use go() and stop() and calculate how long to sleep 
        manually.  

        2. If the robot runs straight into an obstacle (left and right bumpers 
        sensed), then back up. Choose a sensible distance to back up: enough 
        to get away from the obstacle, but not enough to back up into another 
        obstacle. You may then go on to the next random turn and move (in other 
        words, you don't have to try to complete the move that was blocked).  

        3. If the robot runs into an obstacle at an angle such that only the 
        left bumper senses it, then backup and turn clockwise (for your 
        sensible choice of an angle). Then execute the next random turn and 
        move.  

        4. If the robot runs into an obstacle at an angle such that only the 
        right bumper senses it, then backup and turn counter-clockwise (for 
        your sensible choice of an angle). Then execute the next random turn 
        and move.

* cliff_sensors.py:

  - a function cliff_sensors() requires you to read four sensors and control 
    two LED actuators:

    * The front left and front right cliff sensors as an analog values
    * The left and right bumpers as digital values (to determine the program end)
    * The Play and Advance LEDs

    Read the front left and front right cliff sensors while moving a black line 
    below the sensors.  Print out the black line PDF and use it for testing.  
    The location of the black line controls the state of the Play and Advance LEDs.

    When the black line is below the front right cliff sensor the Play LED should 
    be off.  When the black line is below the left cliff sensor the Advance LED 
    should be off.  When the black line is not below the sensor the corresponding 
    LED should be on.

    In addition to the LEDs, print out the value of the analog sensor to the 
    computer display using print.  In fact you should probably do the printing 
    part first!  Since you will need to know where to set the threshold value 
    to decide when the black line is present or absent for the LEDs, you will 
    need to know the range of light and dark values.  The values of both 
    sensors should print to the screen every 0.1 seconds using a well formatted 
    print message.  

    For my program it was simply: Cliff Sensors FL = 80 FR = 720.  
    This line was taken while the black line was below the Front Left Cliff Sensor.  
    Make note of what the white and black values are for your program for each 
    sensor.  The printing of the cliff sensor values and controlling of the LEDs 
    should continue inside a while loop until the user pushes either the left or 
    right bumper.  When a bumper press is observed the program should shutdown 
    the robot and print a Goodbye message to the screen.

* sense.py:

  - a function to print out sensors key, value pairs.

* Pygame install with python3.1::

    $ sudo apt-get install python3.1-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev libportmidi-dev
    $ svn co svn://seul.org/svn/pygame/trunk pygame
    $ cd pygame/
    $ python3.1 setup.py build
    $ sudo python3.1 setup.py install

* Running tests, the discover module looks for modules in the current folder or subfolder with names that start with test:

    * Python 3.1 or earlier: python3 -m discover
    * Python 3.2 or later: python3 -m unittest discover 
