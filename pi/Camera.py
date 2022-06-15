#sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libgstreamer1.0.0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
#pip3 install opencv-python
import cv2

# Function: initcam
# Inputs:
# Outputs:
def initcam():
	print("Initialising camera...")
	camera = cv2.VideoCapture(0)
	camera.set(cv2.CAP_PROP_BUFFERSIZE,1)
	if camera.isOpened:
		print("Camera started")
	else:
		print("Camera not working")
	cv2.startWindowThread()
	stagedpic = "stagedpic"
	cv2.namedWindow(stagedpic)
	startpic = "startpic"
	cv2.namedWindow(startpic)
	splitpic = "splitpic"
	cv2.namedWindow(splitpic)
	finishpic = "finishpic"
	cv2.namedWindow(finishpic)

# Function: takephoto
# Inputs:
#   beamid(string)
#       Location to take a photo
# Outputs:
#   Writes a file to images/
def takephoto(beamid):
	print("Taking photo at "+beamid)
	ret, image = camera.read()
	ret, image = camera.read()
	if not ret:
		print("No image returned")
	cv2.imshow(beamid,image)
	cv2.imwrite("images/"+beamid+str(round(time.time(),0))+".jpg",image)
	camera.release
