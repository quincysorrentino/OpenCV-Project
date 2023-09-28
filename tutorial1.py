import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
    
    #import your image 
img = cv2.imread('assets/red.png', 1)

img = cv2.resize(img, (800, 800))

while True:

#convert the image from the BGR color scheme to HSV
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#set lower and upper values for color filter 
    lower_orange = np.array([0, 0, 138])
    upper_orange = np.array([40, 150, 225])


#create a color mask using inRange() 
    colorMask = cv2.inRange(img, lower_orange, upper_orange)

#use bitwise to remove all irrelivant pixles
    result = cv2.bitwise_and(img, img, mask=colorMask)

# #change the image to greyscale 
    grayImage = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
    
     #apply canny edge detection
    cannyed_image = cv2.Canny(grayImage, 50, 100)
    
#     #display the canny edge image using the matplotlib library
#     #plt.figure()
#     #plt.imshow(cannyed_image, cmap='gray')
#     #plt.show()
    cv2.imshow('canny', cannyed_image)

#    cv2.imshow('result', result)

#if "q" key is pressed then break loop and destroy all windows 
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()










    


