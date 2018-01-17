import cv2
import numpy as np

img = cv2.imread('/home/iot/Downloads/redhat.jpg')
#hsv = hue saturation and value
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([150,160,5])
upper_red = np.array([180,255,150])

#if the mask is in range the value of mask is 1 else 0
mask = cv2.inRange(hsv,lower_red,upper_red)
res = cv2.bitwise_and(img,img, mask = mask)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()



