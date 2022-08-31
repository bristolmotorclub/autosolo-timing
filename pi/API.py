import json # for json.  Obvs
import requests # for posting data to API

# Function: sendtime
# Inputs:
#   beamid(string)
#       Name of beam to update:
#			stage
#			start
#			finish
#			cancelFinish
#			reset
#   thistrigger(string)
#       Timestamp for start/finish
#		Driver number to stage
#   baseURL(string)
#       URL of API
# Outputs:
#   TriggeredInput(string)
#       Name of input that was triggered
#   TriggeredTime(int)
#       Time since midnight that the input was triggered
def sendtime(beamid,thistrigger,baseURL):
	webstatus = "69"
	print("API send function: recording "+beamid+" at "+thistrigger)

	# Code to send stuff
	URL=""
	if beamid == "stage":
		timestampjson = '{"id":'+thistrigger+'}'
		URL = baseURL+'stage'
	if beamid == "start":
		timestampjson = '{"startTime":'+thistrigger+'}'
		URL = baseURL+'start'
	if beamid == "finish":
		timestampjson = '{"finishTime":'+thistrigger+'}'
		URL = baseURL+'finish'
	if len(URL) > 0:
		print(URL)
		uploaddata = json.loads(timestampjson)
		reqheaders = {'Content-Type':'application/json'}
		request = requests.post(url=URL,json=uploaddata,headers=reqheaders)
		webstatus = str(request.status_code)
		print(request)

	# Append to log ... needs datestamp as file prefix
	with open("timinglog.log","a") as logfile:
		logfile.write(thistrigger+","+beamid+","+webstatus+"\n")
		logfile.close
	
	return webstatus
