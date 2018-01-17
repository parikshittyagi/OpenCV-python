import cv2
import numpy as np

img = cv2.imread('/home/iot/Downloads/redhat.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([50,60,5])
upper_red = np.array([255,255,250])

mask = cv2.inRange(hsv,lower_red,upper_red)
res = cv2.bitwise_and(img,img, mask = mask)

kernel = np.ones((5,5), np.uint8)
#all pixels near boundary will be discarded depending upon the size of kernel
erosion = cv2.erode(mask,kernel,iterations = 1)

#it works opposite of erosion, hence after the removal of white noises of image dilation is used to regain the size of image 
dilation = cv2.dilate(mask, kernel, iterations = 1)

#another function of erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#Reverse of Opening,dilation followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#cv2.imshow('img',img)
#cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

