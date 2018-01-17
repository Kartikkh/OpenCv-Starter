import cv2
import numpy as np

# For Loading Images use imread('Name of Image')
image = cv2.imread('image.jpg')
# For Showing Image by this HelloWorld Name
cv2.imshow('helloWorld' , image)

# This will allow you to input information when image window is open
# by leaving it blank it just wait for anykey to be pressed before continuing
## we can place argument (except 0 for 0 it will wait forever to exit for key press ) we can specify the delay ,
#  how long to keep the window open
cv2.waitKey()

# this close all the open windows
# failure of this will make the program in hung state
cv2.destroyAllWindows()


# this show image is 1080Pixel in height, 1920 pixel wide and is having 3 colours (RGB)
print image.shape


print 'Height of Image' , image.shape[0], 'pixel'
print 'Width of Image' , image.shape[1], 'pixel'


