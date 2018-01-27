import numpy as np
import cv2


#Image Interpolation
#http://www.americaswonderlands.com/image_resizing.htm
#Photo interpolation is the process by which the number of pixels comprising an image
#is increased to allow printing enlargements that are of higher quality than photos that are not interpolated.
#Interpolation is commonly needed to make quality large prints from digital photos and film-scanned images.


image = cv2.imread('image.jpg')

#image will be 3/4 size of original image
# cv2.resize takes image , Dimensions of output image , scale factor f and fy , interpolated method
# Interpolated Methods are
#cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) &
# cv2.INTER_LINEAR for zooming.
# By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes
image_scaled = cv2.resize(image , None , fx= 0.75 , fy=0.75)
cv2.imshow("Scaled Image " , image_scaled)
cv2.waitKey()



#image will be double the size of original image
image_scaled = cv2.resize(image , None , fx= 2 , fy=2 , interpolation = cv2.INTER_CUBIC)
cv2.imshow("Scaled Image " , image_scaled)

cv2.waitKey()





#  Resize to given Dimensions replace None by Dimensions
image_scaled = cv2.resize(image , (900,400) , fx= 2 , fy=2 , interpolation =cv2.INTER_AREA)
cv2.imshow("Scaled Image " , image_scaled)

cv2.waitKey()
cv2.destroyAllWindows()

