import numpy as np
import cv2

img = cv2.imread('/home/iot/Downloads/watch.jpg',cv2.IMREAD_COLOR)

'''px =img[10,15] #color value of the location of that pixel

print(px)  #to show the color of pixel

img[10,15] = [0,255,255] #changing the color of pixel into white

print(px) #pixel color changed to white color

print(img[50:100,100:150]) #this will print the color in range of these pixels
'''

img[50:100,100:150] = [255,255,255]

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

