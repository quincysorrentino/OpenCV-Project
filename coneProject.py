#Import required libraries
import cv2
import numpy as np

########################################################## METHODS ##############################################################################

# define the draw_lines function, setting color and thickness
def draw_lines(img, lines, color=[0, 0, 255], thickness=2):
    
    if lines is None:
        return img  
    
# Create a blank image that matches the original in size.
    line_img = np.zeros_like(img, dtype=np.uint8)
    #Find the height of the image 
    height = img.shape[0]

# Loop over all lines and draw them from the top to the bottom of the image.
    for line in lines:
        for x1, y1, x2, y2 in line:
# Calculate the extended points at the top and bottom of the image
            extended_x1 = int(x1 - (y1 - 0) * (x2 - x1) / (y2 - y1))
            extended_x2 = int(x2 - (y2 - height) * (x2 - x1) / (y2 - y1))
                
# Draw the line from top to bottom
            cv2.line(line_img, (extended_x1, 0), (extended_x2, height), color, thickness)

# Merge the image with the lines onto the original.
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    
    return img

########################################################### METHODS ##############################################################################

############################################################# MAIN ###############################################################################

#import the image 
img = cv2.imread('assets/red.png', 1)

#resize the image so it fits on my computer screen (testing purposes)
img = cv2.resize(img, (800, 800))


while True:

#set lower and upper values for color filter 
    lower_orange = np.array([20, 10, 150])
    upper_orange = np.array([50, 120, 240])

#create a color mask using inRange() filled with the upper and lower parameters declared above 
    colorMask = cv2.inRange(img, lower_orange, upper_orange)
 
    kernel = np.ones((5,5),np.uint8)
#use the closing effect to fill in blank spots missed by the color map
#this is done so shapes are filled instead of spotty
    closing = cv2.morphologyEx(colorMask, cv2.MORPH_CLOSE, kernel)

#use bitwise to remove all irrelivant pixles
    result = cv2.bitwise_and(closing, closing, mask=colorMask)
    
#apply canny edge detection to detect clone edges
    cannyed_image = cv2.Canny(closing, 50, 100)

#use HoughLinesP() with various parameters to detect lines (Took forever to get the parameters right)
    lines = cv2.HoughLinesP(cannyed_image, rho=5, theta=np.pi / 180, threshold=86, lines=np.array([]), minLineLength=330, maxLineGap=200)

    if lines is not None:  
# Draw the detected lines on the image
        img = draw_lines(img, lines)

#Display the image      
    cv2.imshow('result', img)
    
#This print statement can be used to show the arrays for the lines and how many lines were drawn (2)  
#print(lines)

#if "q" key is pressed then break loop and destroy all windows 
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()



