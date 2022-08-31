# Function: sendtime
# Inputs:
#   beamid(string)
#       Name of beam to update
#   thistrigger(string)
#       Timestamp of beam
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
	if beamid == "started":
		timestampjson = '{"startTime":'+thistrigger+'}'
		URL = baseURL+'/start'
	if beamid == "finished":
		timestampjson = '{"finishTime":'+thistrigger+'}'
		URL = baseURL+'/finish'
	if len(URL) > 0:
		uploaddata = json.loads(timestampjson)
		reqheaders = {'Content-Type':'application/json'}
		request = requests.post(url=URL,json=uploaddata,headers=reqheaders)
		webstatus = str(request.status_code)

	# Append to log ... needs datestamp as file prefix
	with open("timinglog.log","a") as logfile:
		logfile.write(thistrigger+","+beamid+","+webstatus+"\n")
		logfile.close
	
	return webstatus
