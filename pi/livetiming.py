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

def SetPinMap():
	return "Not Yet Written"

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
	sendtime("stage",str(driver),baseURL)
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
	
