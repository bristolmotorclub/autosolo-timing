#python3

from FDS import DecodeRaw,ReadFDS # FDS functions
from API import sendtime,GetStaged # Connects to Mabware API
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
		# Read in car number from command line
		driver = input("Enter driver number:")
		sendtime("stage",str(driver),baseURL)
	elif StageMethod == "Remote":
		# Get the list of staged cars from server
		staged=GetStaged(baseURL)
		while len(staged) == 2: # wait until there's more than just the two brackets returned
			print("Waiting for car: ")
			time.sleep(1)
			staged=GetStaged(baseURL)
		if '[]' not in staged: # Get the first driver number
			driver = int(staged.split('[')[1].split(',')[0].split(']')[0].split('"')[1])
			print(driver)
	else:
		return 69
	return driver # return the driver number of the first staged car
	

print("Ready for signal")
driver = 0

# Loop forever
while True:
	#Loop forever waiting for interrupt
	#time.sleep(1e6)

	# Test each trigger in turn
	#driver=driver+1 # auto-increment driver number
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
		FDSresult=ReadFDS(config['FDS']['SerialPort'])
		if config['BEAMS']['StartType'] == "FDS":
			if config['BEAMS']['StartID'][1] in FDSresult[0]:
				sendtime("start",FDSresult[1],baseURL)
		if config['BEAMS']['FinishType'] == "FDS":
			if config['BEAMS']['FinishID'][1] in FDSresult[0]:
				sendtime("finish",FDSresult[1],baseURL)