import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt #pip install paho-mqtt

import cv2
camera = cv2.VideoCapture(0)
cv2.namedWindow("frame")
image = camera.read()
cv2.imshow("frame",image)
camera.release

#from picamera import PiCamera
#camera = PiCamera()
#camera.start_preview()
#time.sleep(10)
#camera.capture('image.jpg')
#camera.stop_preview()

# Set mode of GPIO
GPIO.setmode(GPIO.BOARD)
Stage = 16 #GPIO23
Start = 18 #GPIO24
Finish = 22 #GPIO25
Split = 24 #GPIO8
GPIO.setwarnings(False)
GPIO.setup(Stage, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Start, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Finish, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Split, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Staged interrupt function
def staged(pin):
	global stagetrigger
	if time.time() - stagetrigger < 1: # Probably a double-trigger
			print "too soon!"
	else: # Seems a valid trigger
		print "Staged!"

# Start interrupt function
def started(pin):
	global starttrigger
	if time.time() - starttrigger < 1: # Probably a double-trigger
			print "too soon!"
	else: # Seems a valid trigger
		starttrigger = time.time()
		print "Start timestamp: " + str(starttrigger)
		#publish to broker
		#client.publish("StartLine", payload=trigger, qos=0, retain=False)

# Split interrupt function
def splitted(pin):
	global splittrigger
	if time.time() - splittrigger < 1: # Probably a double-trigger
			print "too soon!"
	else: # Seems a valid trigger
		splittime = time.time() - starttrigger
		splittrigger = time.time()
		print "Split time: " + str(round(splittime,2)) + "s"

# Finish interrupt function
def finished(pin):
	global finishtrigger
	if time.time() - finishtrigger < 1: # Probably a double-trigger
			print "too soon!"
	else: # Seems a valid trigger
		finishtime = time.time() - starttrigger
		finishtrigger = time.time()
		print "Finish time: " + str(round(finishtime,2)) + "s"
		

# Initialise trigger timestamp
stagetrigger = time.time()
starttrigger = time.time()
splittrigger = time.time()
finishtrigger = time.time()

# Set interrupt function for GPIO (pin, rising/falling, function)
# Use falling for testing without a reflector
# Use rising for beam break with refector
GPIOstate = GPIO.FALLING
GPIO.add_event_detect(Start, GPIOstate, started)
GPIO.add_event_detect(Stage, GPIOstate, staged)
GPIO.add_event_detect(Split, GPIOstate, splitted)
GPIO.add_event_detect(Finish, GPIOstate, finished)

# Connect to broker
#client = mqtt.Client()
#client.on_connect = 
#client.loop_forever() # Loop to maintain connection

print "Ready for signal"

# Loop forever
while True:
	time.sleep(1e6)
