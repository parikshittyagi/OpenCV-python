#this code elaborates the loading of an image and showing it on screen

import cv2
import numpy as np
import matplotlib.pyplot as plt
#cv2.imread used for reading the image.IMREAD_GRAYSCALE is used to convert the image into gray so that loading is done quickly
img = cv2.imread('/home/iot/Downloads/watch.jpg',cv2.IMREAD_GRAYSCALE) 
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

'''cv2.imshow('image',img) #showing the image
cv2.waitKey(0)         #the image waits till any key is pressed  
cv2.destroyAllWindows() #it closes the image when a key is pressed '''

plt.imshow(img,cmap='gray',interpolation='bicubic') #to show image in a graphical way and color gray
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

cv2.imwrite('watchgray.jpg',img) #it saves the image
