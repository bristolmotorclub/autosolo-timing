#python3

import RPi.GPIO as GPIO
import time
#import paho.mqtt.client as mqtt #pip3 install paho-mqtt

#sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libgstreamer1.0.0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
#pip3 install opencv-python
import cv2
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_BUFFERSIZE,1)
if camera.isOpened:
	print("Camera started")
else:
	print("Camera not working")
cv2.startWindowThread()
stagedpic = "stagedpic"
#cv2.namedWindow(stagedpic)
startpic = "startpic"
cv2.namedWindow(startpic)
splitpic = "splitpic"
#cv2.namedWindow(splitpic)
finishpic = "finishpic"
cv2.namedWindow(finishpic)

# Set mode of GPIO
GPIO.setmode(GPIO.BOARD)
#Stage = 16 #GPIO23
#Start = 18 #GPIO24
#Finish = 22 #GPIO25
Split = 24 #GPIO8
Start = 16
Finish = 18
Stage = 22
GPIO.setwarnings(False)
GPIO.setup(Stage, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Start, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Finish, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Split, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to send data to web service
def sendtime(beamid,timestamp):
	# Code to send stuff
	# Append to log ... needs datestamp as file prefix
	with open("timinglog.log","a") as logfile:
			logfile.write(timestamp+","+beamid)

# Staged interrupt function
def staged(pin):
	global stagetrigger
	if time.time() - stagetrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		print("Staged!")
		ret, image = camera.read()
		ret, image = camera.read()
		if not ret:
			print("No image returned")
		cv2.imshow(stagedpic,image)
		camera.release

# Start interrupt function
def started(pin):
	global starttrigger
	if time.time() - starttrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		starttrigger = time.time()
		print("Start timestamp: " + str(starttrigger))
		ret, image = camera.read()
		ret, image = camera.read()
		if not ret:
			print("No image returned")
		cv2.imshow(startpic,image)
		camera.release
		#publish to broker
		#client.publish("StartLine", payload=trigger, qos=0, retain=False)

# Split interrupt function
def splitted(pin):
	global splittrigger
	if time.time() - splittrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		splittime = time.time() - starttrigger
		splittrigger = time.time()
		print("Split time: " + str(round(splittime,2)) + "s")
		ret, image = camera.read()
		ret, image = camera.read()
		if not ret:
			print("No image returned")
		cv2.imshow(splitpic,image)
		camera.release

# Finish interrupt function
def finished(pin):
	global finishtrigger
	if time.time() - finishtrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		finishtime = time.time() - starttrigger
		finishtrigger = time.time()
		speed = 0.1/finishtime*3.6/8*5
		print("Finish time: " + str(round(finishtime,2)) + "s")
		print("Speed: "+str(round(speed,2))+"mph")
		ret, image = camera.read()
		ret, image = camera.read()
		if not ret:
			print("No image returned")
		cv2.imshow(finishpic,image)
		cv2.imwrite("images/"+str(round(time.time(),0))+".jpg",image)
		camera.release

# Initialise trigger timestamp
stagetrigger = time.time()
starttrigger = time.time()
splittrigger = time.time()
finishtrigger = time.time()

# Set interrupt function for GPIO (pin, rising/falling, function)
# Use falling for testing without a reflector
# Use rising for beam break with refector
GPIOstate = GPIO.RISING
GPIO.add_event_detect(Start, GPIOstate, started)
GPIO.add_event_detect(Stage, GPIOstate, staged)
GPIO.add_event_detect(Split, GPIOstate, splitted)
GPIO.add_event_detect(Finish, GPIOstate, finished)

# Connect to broker
#client = mqtt.Client()
#client.on_connect = 
#client.loop_forever() # Loop to maintain connection

print("Ready for signal")

# Loop forever
while True:
	time.sleep(1e6)
