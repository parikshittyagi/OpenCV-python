import cv2
import numpy as np

img = cv2.imread('/home/iot/Downloads/redhat.jpg')
#hsv = hue saturation and value
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([50,60,5])
upper_red = np.array([255,255,250])

#if the mask is in range the value of mask is 1 else 0
mask = cv2.inRange(hsv,lower_red,upper_red)
res = cv2.bitwise_and(img,img, mask = mask)

#np.ones((pixels,pixels),np.float32)/pixel*pixel
kernel = np.ones((15,15), np.float32)/225
#smoothed is used to apply simple average of pixels
smoothed = cv2.filter2D(res, -1, kernel)

#gaussian Blur : In this we specify height and width of kernel which should be ppositive and odd
blur = cv2.GaussianBlur(res, (15,15), 0)
#medianBlur is the least noisy 
median = cv2.medianBlur(res,15)
bilateral = cv2.bilateralFilter(res,15,75,75)


#cv2.imshow('smoothed',smoothed)
#cv2.imshow('img',img)
#cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('blur',blur)
cv2.imshow('median',median)
cv2.imshow('bilateral',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
