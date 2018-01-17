import numpy as np
import cv2

img = cv2.imread('/home/iot/Downloads/watch.jpg',cv2.IMREAD_COLOR)  #Create a black image

#Draw a diagonal blue line with thickness of 5 px

#(image_name,origin,end,color,thickness)
cv2.line(img,(0,0),(150,150),(255,0,0),5)

#(image_name,left_upper_corner,right_buttom_corner,color,thickness)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),3)

#(image_name,circle_center,radius,color,thickness)
cv2.circle(img,(100,100),63,(0,0,255),-10)

#creating an array from numpy function and defining the coordinates
pts = np.array([[10,20],[20,40],[60,14],[80,45]],np.int32)
#(image_name,points,To connect last and first point or not),color,thickness)
cv2.polylines(img,[pts],False,(0,255,255),5)

#defining the font of the text to be written on image
font = cv2.FONT_HERSHEY_SIMPLEX
#(image_name,text to be written,start & end of text,font,size,color,thickness)
cv2.putText(img,'OpenCV',(0,130),font,1,(200,255,0),2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
