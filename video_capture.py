import cv2
import numpy as np

cap = cv2.VideoCapture('/home/iot/Downloads/Sample_Video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DVID')
out = cv2.VideoWriter('Sample_Video',fourcc,20.0,(640,480))

while (cap.isOpened()): #till the video stops
	ret, frame = cap.read()  #video is converted into frames and captured frame by frame, also cap.read returns boolean function
	if ret==True:
		frame = cv2.flip(frame,0)
		#write the flipped frame		
		out.write(frame)

	#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #frames converted in gray

	cv2.imshow('frame',frame) 

	if cv2.waitKey(1) & 0xFF == ord('q'): #exit from loop
		break

	else:
		break

cap.release()   #always lease the cap 
out.release() 
cv2.destroyAllWindows() #close all the windows opened in the program
