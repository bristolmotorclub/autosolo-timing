# Overview
Some boiler-plate code to upload timestamps recorded from GPIO or FDS timing gear to a web server.

## Things still to do...
* Tests
* Make it work!

## livetiming.py
The main code to bring the functions together

### Still to do...
* Only works with FDS timing
* Doesn't support splits

## API.py
Pushes times to the web service (https://github.com/mabware/timing-reconciliation-api)

## Camera.py
Some old code for reading images from a camera to correlate with triggers

## FDS.py
Functions for connecting to the FDS Timing hardware and returning the time stamp and input when triggered.

## GPIO.py
Functions for reading times directly from GPIO pins.

## livetiming.py
Some old code for reading from GPIO pins.

## build.sh
Copies the python code to a folder and appends the command line to rc.local.

### Bugs
* Doesn't check if it's already in rc.local
* Not checked it even works!  Better off doing this manually.