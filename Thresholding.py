import cv2
import numpy as np

img = cv2.imread('/home/iot/Downloads/bookpage.jpg')
#########################SIMPLE THRESHOLDING####################################


#(image_name,threshold value, highest value, cv2.THRESHOLD_BINARY)
#retval, threshold1 = cv2.threshold(img, 12, 255,cv2.THRESH_BINARY)
#retval, threshold2 = cv2.threshold(img, 12, 255,cv2.THRESH_BINARY_INV)
#retval, threshold3 = cv2.threshold(img, 12, 255,cv2.THRESH_TRUNC)
#retval, threshold4 = cv2.threshold(img, 12, 255,cv2.THRESH_TOZERO)
#retval, threshold5 = cv2.threshold(img, 12, 255,cv2.THRESH_TOZERO_INV)

############################ADAPTIVE THRESHOLDING###############################
#cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is mean of neif=ghbourhood area
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is weighted sum of neighbourhood values where weights are a gaussian window

#gaus1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#mean = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

#grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#retval2, threshold2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)

#gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)

################################OTSU'S BINARIZATION##########################
#OTSU's : It automatically calculate threshold value from image histogramfor aa bimodal binarization i.e in THRESHOLD value we simply pass 0 and computer automatically takes value 

retval2, otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(grayscaled,(5,5),0)

retval2, otsu1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('original',img)
#cv2.imshow('threshold1', threshold1)
#cv2.imshow('threshold2',threshold2)
#cv2.imshow('threshold3',threshold3)
#cv2.imshow('threshold4',threshold4)
#cv2.imshow('threshold5',threshold5)
#cv2.imshow('gaus',gaus)
#cv2.imshow('gaus1',gaus)
#cv2.imshow('mean',mean)
cv2.imshow('otsu',otsu)
cv2.imshow('otsu1',otsu1)

cv2.waitKey(0)
cv2.destroyAllWindows()
