#python3

from API import sendtime # Library for connecting to the API
from FDS import DecodeRaw,ReadFDS # (FDS function)
import configparser # Library for importing config (https://docs.python.org/3/library/configparser.html)
import time # for sleeping (testing only, I guess)

print("Importing config")
config=configparser.ConfigParser()
config.read('.\config.ini')

def SetPinMap():
	return "Not Yet Written"

print(config['Start']['type'])
print(config['Start']['port'])

# Loop forever
while True:
	# Read all inputs
	FDSread = ReadFDS(config['Start']['port'])
	if FDSread[0] == config['Start']['input']:
		print("start detected at "+str(FDSread[1]))
		sendtime("start",str(FDSread[1]),config['Server']['serverURL'])
	elif FDSread[0] == config['Finish']['input']:
		print("finish detected at "+str(FDSread[1]))
		sendtime("finish",str(FDSread[1]),config['Server']['serverURL'])