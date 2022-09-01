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
# Configure staging
StageMethod = config['STAGE']['StageMethod']
if 'GreenLightPin' in config:
	GreenLightPin = config['STAGE']['GreenLightPin']
	GreenLightMethod = config['STAGE']['GreenLightMethod']

def ReadTest():
	time.sleep(2)
	TriggeredInput="1"
	TriggeredTime=str(time.time())
	print(TriggeredInput,TriggeredTime)
	return (TriggeredInput,TriggeredTime)

def SetPinMap():
	return "Not Yet Written"
	
def StageCar():
	global driver
	if StageMethod == "Local":
		# Read in car number
		driver = input("Enter driver number:")
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
	driver=driver+1
	print("Staging car")
	StageCar()
	if config['BEAMS']['StartType'] == "Test":
		Start=ReadTest()
		sendtime("start",Start[1],baseURL)
	if config['BEAMS']['FinishType'] == "Test":
		Finish=ReadTest()
		sendtime("finish",Finish[1],baseURL)
	if 'FDS' in config:
		print("Reading FDS")
		#Start=ReadFDS()
	
