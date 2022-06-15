# Demo script to pull data from FDS timing device plugged in via USB

import serial
import datetime
import time

# Function: DecodeRaw
# Inputs:
#   rawtiming(byte)
#       Raw bytes from the serial port
# Outputs:
#   TriggeredInput(string)
#       Name of input that was triggered
#   TriggeredTime(int)
#       Time since midnight that the input was triggered
def DecodeRaw(rawtiming):
    utftime = rawtiming[0:len(rawtiming)-2].decode("utf-8")
    TimeSplitArray = utftime.split()
    TriggeredInput = TimeSplitArray[2]
    TimeString = TimeSplitArray[3]
    TimeArray = time.strptime(TimeString.split('.')[0],'%H:%M:%S')
    TriggeredTime = datetime.timedelta(hours=TimeArray.tm_hour,minutes=TimeArray.tm_min,seconds=TimeArray.tm_sec).total_seconds() + int(TimeString.split('.')[1])/100000
    print(TriggeredInput,TriggeredTime)
    return (TriggeredInput,TriggeredTime)

# Function: ReadFDS
# Inputs:
#   SerialPort(string)
#       Name of serial port (e.g. COM3 or /dev/tty)
# Outputs:
#   ThisTime(array)
#       (string)Name of input that was triggered
#       (int)Time since midnight that the input was triggered
def ReadFDS(SerialPort):
    ser = serial.Serial(SerialPort,9600,timeout=1)
    print("Connected to " + ser.name)
    rawtiming = ""
    while not rawtiming:
        rawtiming = ser.readline()
        if rawtiming:
            ThisTime = DecodeRaw(rawtiming)
    ser.close()
    return ThisTime
