import numpy as np
import cv2

image = cv2.imread('image.jpg')

# HSV is another color scheme like RGB . Useful in OpenCV for color segmentation
# In RGB, Filtering is not a easy task , however HSV makes it super easy to set color ranges to filter specific color
# HSV is named as such for three values: hue, saturation, and value.
# H stands for Hue --> Color (0-179)
# S stands for saturation --> Vibrancy of color (0-255)
# V stands for Value --> Brightness of Color (0-255)


# Converting Image from BGR to HSV
Hsv_Image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

## showing HSV Image
cv2.imshow('HSV Image' , Hsv_Image)

# we take hue channel for all heights and width.
cv2.imshow('Hue Channel' , Hsv_Image[ :, :, 0])

# we take Saturation  channel for all heights and width.
cv2.imshow('Saturation channel' , Hsv_Image[:,:,1])

# we take Value channel for all heights and width.
cv2.imshow('Value Image' , Hsv_Image[:,:,2])

cv2.waitKey(0)



# this close all the open windows
# failure of this will make the program in hung state
cv2.destroyAllWindows()

# Note - imshow function only show the image in BGR format !
