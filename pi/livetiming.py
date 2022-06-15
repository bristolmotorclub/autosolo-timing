#python3

from FDS.py import DecodeRaw,ReadFDS # (FDS function)
import time # for sleeping (testing only, I guess)
import json # for json.  Obvs
import requests # for posting data to API

# Set base URL for API
baseURL = 'http://path.to/API'

def SetPinMap():
	return "Not Yet Written"

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
	
