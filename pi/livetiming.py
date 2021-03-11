#python3

import RPi.GPIO as GPIO
import time
#import paho.mqtt.client as mqtt #pip3 install paho-mqtt (currently using JSON to web API rather than MQTT)

import json # forjson.  Obvs

# Camera initialisation (commented out for the future)
#sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libgstreamer1.0.0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
#pip3 install opencv-python
#import cv2
#camera = cv2.VideoCapture(0)
#camera.set(cv2.CAP_PROP_BUFFERSIZE,1)
#if camera.isOpened:
#	print("Camera started")
#else:
#	print("Camera not working")
#cv2.startWindowThread()
#stagedpic = "stagedpic"
#cv2.namedWindow(stagedpic)
#startpic = "startpic"
#cv2.namedWindow(startpic)
#splitpic = "splitpic"
#cv2.namedWindow(splitpic)
#finishpic = "finishpic"
#cv2.namedWindow(finishpic)

# Configure GPIO mode/pins
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

# Function to send data to web service
def sendtime(beamid,thistrigger):
	thistrigger=str(thistrigger)
	print("API send function: recording "+beamid+" at "+thistrigger)

	# Code to send stuff
	timingdata = '{"beamid":"'+beamid+'","timestamp":"'+thistrigger+'"}'
	uploaddata = json.loads(timingdata)
	URL = 'https://path.to/API'
	reqheaders = {'Content-Type':'application/json'}
	#request = requests.post(url=URL,json=uploaddata,headers=reqheaders)

	# Append to log ... needs datestamp as file prefix
	with open("timinglog.log","a") as logfile:
#			logfile.write(thistrigger+","+beamid+","+request.status_code)
			logfile.write(thistrigger+","+beamid+",")

# Staged interrupt function
def staged(pin):
	global stagetrigger
	if time.time() - stagetrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		sendtime("staged",str(time.time()))
		print("Staged!")
		
		# Take a photo of staged car (future)
		#ret, image = camera.read()
		#ret, image = camera.read()
		#if not ret:
		#	print("No image returned")
		#cv2.imshow(stagedpic,image)
		#camera.release

# Start interrupt function
def started(pin):
	global starttrigger
	if time.time() - starttrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		starttrigger = time.time()
		sendtime("started",str(starttrigger))
		print("Start timestamp: " + str(starttrigger))
		
		# Take a photo of starting car (future)
		#ret, image = camera.read()
		#ret, image = camera.read()
		#if not ret:
		#	print("No image returned")
		#cv2.imshow(startpic,image)
		#camera.release
		
		#publish to broker (currently using web API)
		#client.publish("StartLine", payload=trigger, qos=0, retain=False)

# Split interrupt function
def splitted(pin):
	global splittrigger
	if time.time() - splittrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		splittrigger = time.time()
		sendtime("split",str(splittrigger))
		splittime = splittrigger - starttrigger
		print("Split time: " + str(round(splittime,2)) + "s")

		# Take a photo of car (future)
		#ret, image = camera.read()
		#ret, image = camera.read()
		#if not ret:
		#	print("No image returned")
		#cv2.imshow(splitpic,image)
		#camera.release

# Finish interrupt function
def finished(pin):
	global finishtrigger
	if time.time() - finishtrigger < 1: # Probably a double-trigger
		print("too soon!")
	else: # Seems a valid trigger
		finishtrigger = time.time()
		sendtime("finished",str(finishtrigger))

		# Calculate elapsed time and log timestamp
		finishtime = finishtrigger - starttrigger
		#calculate speed based on 100mm distance between gates
		speed = 0.1/finishtime*3.6/8*5
		print("Finish time: " + str(round(finishtime,2)) + "s")
		print("Speed: "+str(round(speed,2))+"mph")

		# Take a photo of car (future)
		#ret, image = camera.read()
		#if not ret:
		#	print("No image returned")
		#cv2.imshow(finishpic,image)
		#cv2.imwrite("images/"+str(round(time.time(),0))+".jpg",image)
		#camera.release

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
	#Loop forever waiting for interrupt
	#time.sleep(1e6)

	# Test each trigger in turn
	time.sleep(2)
	print("pretending to stage")
	staged(0)
	time.sleep(2)
	print("pretending to start")
	started(0)
	time.sleep(2)
	print("pretending to split")
	splitted(0)
	time.sleep(2)
	print("pretending to finish")
	finished(0)
	time.sleep(2)
	
