python-boatd
============

[![BuildStatus](https://travis-ci.org/boatd/python-boatd.png?branch=master)](https://travis-ci.org/boatd/python-boatd)

Python module for writing [boatd](https://github.com/boatd/boatd) behavior
scripts.

## class __Boat__
****************************************
A boat controlled by boatd


### __descriptors__
****************************************
#### __heading__
Return the current heading of the boat in degrees

#### __position__
Return a tuple in the form `(latitude, longitude)`

#### __version__
Return the version of boatd

#### __wind__
Return the direction of the wind in degrees

### __methods__
****************************************
#### def __\__init__\__(self, host='localhost', port=2222):

Create a boat instance, connecting to boatd at `host` on port `port`

#### def __rudder__(self, angle):

Set the angle of the rudder to be `angle` degrees

#### def __sail__(self, angle):

Set the angle of the sail to `angle` degrees

