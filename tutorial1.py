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
    
    
    #cv2.imshow('canny', cannyed_image)

#    cv2.imshow('result', result)

# declare lines and set it to "Auto detect" using HoughLinesP
    lines = cv2.HoughLines(cannyed_image, 1, np.pi/180, 30)

# for each line in lines draw a green line on the x and y cords
#    for line in lines:
 #       x1, y1, x2, y2 = line[0]
 #       cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

    if lines is not None:
        # For each line in lines, draw a green line on the x and y coordinates
        for rho, theta in lines[:, 0]:
            # Convert polar coordinates to Cartesian coordinates
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    cv2.imshow('img', img)

#if "q" key is pressed then break loop and destroy all windows 
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()










    


