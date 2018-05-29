import copy
import numpy as np 

def skyRegion1(image):
	iLow=np.array([100,43,46])
	iHigh=np.array([124,255,255])
	img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

	#hsv split
	h,s,v=cv2.split(img)
	v=cv2.equalizeHist(v)
	hsv=cv2.merge((h,s,v))

	imgThresholded=cv2.inRange(hsv,iLow,iHigh)
	imgThresholded=cv2.medianBlur(imgThresholded,9)

	#open
	kernel=np.ones((5,5),np.uint8)
	imgThresholded=cv2.morphologyEx(imgThresholded,cv2.MORPH_OPEN,kernal,iterations=10)
	imgThresholded=cv2.medianBlur(imgThresholded,9)
	return imgThresholded

def seamClone():
	