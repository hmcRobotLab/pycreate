.. _02setup:

Setup Overview
==============

* Option 1 Teather: directly connected with wire.  Create and computer with serial cable (9pin to usb or rs232) 
* Option 2 Teather and wireless (802.11): Above setup with an additional computer and wireless network needed
* Option 3 Bluetooth: Create and computer wireless connection via bluetooth protocol
* Option 4 Simulator: Computer with create software environment and without the create hardware

Wireless Network
================
* Power on wireless access point and configure

Physical, Startup, Boot, and Connect
====================================
#. Start with robot on open floor space
#. Press power button on robot, verify green led
#. Start robot laptop, configure wireless, and sshd
#. Connect usb to serial cable between robot and robot laptop
#. Secure robot and robot laptop together with velcro
#. Start base laptop, and wireless, then ssh to robot laptop::
    $ ssh -Y from base laptop to access robot laptop.
#. On robot laptop, remotely lookup serial port name connected to robot.  Python needs this variable to make the serial connection::

    $ ls /dev/tty <tab>
    /dev/ttyUSB0 is my connection, yours may differ

Software
========
Clone the latest software to your computer::
    $ git clone git://github.com/mgobryan/pycreate

Add the create.py file to your python path::
    $ sudo cp pycreate/create.py /usr/local/lib/python2.6/site-packages/

Change into the directory with create.py::
    $ cd pycreate
