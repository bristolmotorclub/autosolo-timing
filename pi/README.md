# Overview
livetiming.py uses interrupts to trigger start/finish timing and upload timestamps to server

build.sh installs the script to run at boot

## config.ini
Used for managing configuration of the current event

### [SERVER]
ResultsAPI = https://server.example.com/

## livetiming.py

### Current features
* Records timestamp to a log file
* displays webcam image from last trigger on screen
* Saves picture of all finishers to ./images

### Things still to do...
* Write the code to push to the API (https://github.com/mabware/timing-reconciliation-api)
* Test it
* Tidy everything!

## build.sh
Copies the python code to a folder and appends the command line to rc.local.

### Bugs
* Doesn't check if it's already in rc.local
* Not checked it even works!

## FDS.py
Functions for connecting to the FDS Timing hardware and returning the time stamp and input when triggered.

## GPIO.py
Functions for reading times directly from GPIO pins.

Uses interrupts on several pins to trigger a function for that pin's determined location.  Four pins are defined at the start of the script for the following timing beams:

* Staged (ready to start)
* Start
* Split
* Finish
