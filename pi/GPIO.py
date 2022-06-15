import RPi.GPIO as GPIO
import time
from API.py import SendTime

# Function: GetPinMap
# Inputs:
#   pinmap.db
# Outputs:
#   PinMap(array) strings
def GetPinMap():
    print("Getting pin map...")
    return PinMap

# Function: GPIOTrigger
# Inputs:
#   pin(int)
#       Pin number that was triggered
# Outputs:
#   Sends timestamp to web service
def GPIOTrigger(pin):
	if time.time() - LastTrigger[pin] < 1: # Probably a double-trigger
		print("too soon!")
    else:
        TriggerTime = time.time()
        TriggerTime = str(round(TriggerTime*1000))
        PinMap = GetPinMap()
        LastTrigger[pin] = TriggerTime
        SendTime(PinMap(pin),TriggerTime)

def InitGPIO(BeamPins):
    BeamPins = (16,18,22,24) #GPIO 23,24,25,8
    # Configure GPIO mode/pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(BeamPins[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BeamPins[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BeamPins[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BeamPins[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    global LastTrigger
    InitTime = time.time()

    # Set interrupt function for GPIO (pin, rising/falling, function)
    # Use falling for testing without a reflector
    # Use rising for beam break with refector
    GPIOstate = GPIO.RISING
    for i in range(0,4,1):
        GPIO.add_event_detect(BeamPins[i], GPIOstate, GPIOTrigger(i))
        LastTrigger[i] = InitTime

    return InitTime