import numpy as np
import cv2

img1 = cv2.imread('/home/iot/Downloads/img1.jpeg')
img2 = cv2.imread('/home/iot/Downloads/img2.jpeg')

'''add = img1 + img2
add = cv2.add(img1,img2) #this function adds the pixel of two images
(image_name,weight of img1,image_name,weight of img2,gamma function=0)
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)'''

#we want to put logo on the corner,so created a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]  #region of image

#converting image color to gray
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#creating a mask of logo and its inverse also
ret, mask = cv2.threshold(img2gray, 210, 225, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

#now blacking out the background of image 1
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

#now taking only region of logo from image
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

#putting Logo in ROI and Modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('img1_bg',img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('img2_fg',img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


