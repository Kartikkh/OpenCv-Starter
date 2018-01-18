import numpy as np
import cv2

## Open CV stores value in BRG format


# For Loading Images use imread('Name of Image')
# open CV creates a image array and store all the information
image = cv2.imread('image.jpg')
# For Showing Image by this HelloWorld Name
cv2.imshow('helloWorld' , image)

# Getting Color values from the array
B ,G ,R  = image[0,0]
print B, G, R

# This will allow you to input information when image window is open
# by leaving it blank it just wait for anykey to be pressed before continuing
## we can place argument (except 0 for 0 it will wait forever to exit for key press ) we can specify the delay ,
#  how long to keep the window open

cv2.waitKey()


# convert this to gray Scale and then check

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('GrayScale' , gray_image)
cv2.waitKey(0)

# convert a image into gray scale will gives only two value
# here you see that output only contains Height and Width.
print gray_image.shape

# Gray scale image contains only 1 pixel value ranging from 0-255
print gray_image[1,2]

# this close all the open windows
# failure of this will make the program in hung state
cv2.destroyAllWindows()


