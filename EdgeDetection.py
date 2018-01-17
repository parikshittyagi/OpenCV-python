import cv2
import numpy as np

img = cv2.imread('/home/iot/Downloads/img1.jpeg')

#In laplacian or sobel method we loose edges i.e it is more proficient method for removing noise in the images 
laplacian = cv2.Laplacian(img, cv2.CV_64F)
#Sobel(image name,cv2.CV_64F,x-axis,y-axis, kernel size)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

#It is used to detect edges,here first noise is removed then further process of edge detection is done
#(image_name,min_value,max_value)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('img',img)
#cv2.imshow('laplacian',laplacian)
cv2.imshow('soblex',sobelx)
cv2.imshow('sobley',sobely)
cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

