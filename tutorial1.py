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
    #hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#set lower and upper values for color filter 
    lower_orange = np.array([20, 10, 150])
    upper_orange = np.array([50, 120, 240])


#create a color mask using inRange() 
    colorMask = cv2.inRange(img, lower_orange, upper_orange)
    
    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(colorMask, cv2.MORPH_CLOSE, kernel)

#use as test to display closing effect
    #cv2.imshow('closing', closing)

# #use bitwise to remove all irrelivant pixles
    result = cv2.bitwise_and(closing, closing, mask=colorMask)
    
#      #apply canny edge detection
    cannyed_image = cv2.Canny(closing, 50, 100)
    
    #use as test to cannyed effect
    cv2.imshow('canny', cannyed_image)

# #    cv2.imshow('result', result)

 # declare lines and set it to "Auto detect" using HoughLinesP
    # lines = cv2.HoughLines(cannyed_image, 1, np.pi/180, 30)

    # if lines is not None:
    #     # For each line in lines, draw a green line on the x and y coordinates
    #     for rho, theta in lines[:, 0]:
    #         # Convert polar coordinates to Cartesian coordinates
    #         a = np.cos(theta)
    #         b = np.sin(theta)
    #         x0 = a * rho
    #         y0 = b * rho
    #         x1 = int(x0 + 1000 * (-b))
    #         y1 = int(y0 + 1000 * (a))
    #         x2 = int(x0 - 1000 * (-b))
    #         y2 = int(y0 - 1000 * (a))

    #cv2.line(cannyed_image, (x1, y1), (x2, y2), (0, 255, 0), 1)

    #cv2.imshow('result', cannyed_image)

#if "q" key is pressed then break loop and destroy all windows 
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()



