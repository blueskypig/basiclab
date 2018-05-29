import cv2
import numpy as np
from numba import jit
from PIL import Image,ImageFilter
#from matplotlib import pyplot as plt
from aip import AipFace


def initcamera(index):
	cap=cv2.VideoCapture(index)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
	cap.set(cv2.CAP_PROP_FPS,30)
	return cap
	
fgbg=cv2.createBackgroundSubtractorMOG2()
def backgroundsub(image):

	ximage=fgbg.apply(image);
	return ximage
@jit
def mypro(image):
	#ans=np.flip(image,1)
	timg=Image.fromarray(image)
	ans=timg.filter(ImageFilter.CONTOUR)
	ans=np.array(ans)
	return ans 
	#cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

@jit
def facedetect(image):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray=gray[y:y+h,x:x+w]
		roi_color=image[y:y+h,x:x+w]
		eyes=eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	return image

def baiduface(image):
	APP_ID='10609655'
	API_KEY='4yrvGxBoy5weKhQaEiT42TuF'
	SECRET_KEY='udrrpSRYQxQ6jpu7putDP6gen6AWAGhR'
	client=AipFace(APP_ID,API_KEY,SECRET_KEY)
	options={}
	options['max_face_num']=2
	options['face_fields']="age,gender,beauty,race,"
	
	return client.detect(image,options)


if __name__ =='__main__':

	cap=initcamera(0);
	while(True):
		#get a frame
		ret,image=cap.read()
		cv2.imwrite('tmp.jpg',image)

		#with open('tmp.jpg','rb') as fp:
		#	bimage=fp.read()
		#res=baiduface(bimage)
		#print(res)
		#(x,y,w,h) = res['result'][0]['location'].values()
		#cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		#font = cv2.FONT_HERSHEY_SIMPLEX
		#cv2.putText(image, "age:"+str(res['result'][0]['age']),(10,100),font,1,(255,0,0),1,cv2.LINE_AA)
		ximage=cv2.resize(image[:,:,0],(300,300))
		cv2.imshow('image',ximage)
		
		#ximage=backgroundsub(image)
		
		#gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		
		#ximage=mypro(image)
		#cv2.imshow('ximage',ximage)
		
		'''
		yolo=YOLO_face_tf.YOLO_TF();
		
		yolo.detect_from_cvmat(image);
		'''
		#dst1_gray, dst1_color =cv2.pencilSketch(image, sigma_s = 50, sigma_r = 0.15, shade_factor = 0.04)
		#dst2 = cv2.stylization(image, sigma_s = 50, sigma_r = 0.15)
		#dst3 = cv2.detailEnhance(image, sigma_s = 50, sigma_r = 0.15)
		#dst4 = cv2.edgePreservingFilter(image, flags=1, sigma_s = 50, sigma_r = 0.15)

		## display
		#cv2.imshow("pencilSketchG", dst1_gray)
		#cv2.imshow("pencilSketchC", dst1_color)
		#cv2.imshow("stylization", dst2)
		#cv2.imshow("detailEnhance", dst3)
		#cv2.imshow("edgePreserving", dst4)

		#image=facedetect(image)

		#show a frame
		
		
		if cv2.waitKey(0) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()
