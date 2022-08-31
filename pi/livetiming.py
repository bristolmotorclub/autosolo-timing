#python3

from FDS import DecodeRaw,ReadFDS # FDS functions
from API import sendtime # Connects to Mabware API
import time # for sleeping (testing only, I guess)
import configparser

# import config.ini
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

# Set base URL for API
baseURL = config['SERVER']['ResultsAPI']
# Configure stagiing
StageMethod = config['STAGE']['StageMethod']
if 'GreenLightPin' in config:
	GreenLightPin = config['STAGE']['GreenLightPin']
	GreenLightMethod = config['STAGE']['GreenLightMethod']

def SetPinMap():
	return "Not Yet Written"
	
def StageCar():
	global driver
	if StageMethod == "Local":
		# Read in car number
		driver = driver
	elif StageMethod == "Remote":
		# Wait for car to be staged online
		driver = driver
	else:
		return 69
	sendtime("stage",str(driver),baseURL)
	return driver
	

print("Ready for signal")
driver = 0

# Loop forever
while True:
	#Loop forever waiting for interrupt
	#time.sleep(1e6)

	# Test each trigger in turn
	time.sleep(2)
	driver=driver+1
	print("pretending to stage")
	StageCar()
	time.sleep(2)
	print("pretending to start")
	sendtime("start",str(time.time()),baseURL)
	time.sleep(2)
#	print("pretending to split")
#	sendtime("split")
#	time.sleep(2)
	print("pretending to finish")
	sendtime("finish",str(time.time()),baseURL)
	time.sleep(2)
	
