import numpy as np
import cv2

#For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
#findContours function modifies the source image. So if you want source image even after finding contours,
#already store it to some other variables.
#In OpenCV, finding contours is like finding white object from black background.
#So remember, object to be found should be white and background should be black.



image = cv2.imread('image.jpg')
cv2.imshow("Original" ,  image)
cv2.waitKey()

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimage" ,  grayimage)
cv2.waitKey()

ret, thresh = cv2.threshold(grayimage, 127, 255, 0)
cv2.imshow("thresh" ,  thresh)
cv2.waitKey()
# Finding Edges

CannyEdge = cv2.Canny(thresh,50,100)
cv2.imshow("CannyEdges" ,  CannyEdge)
cv2.waitKey()


#Finding Contours
# Contour is the return list of contour from the image
# it is lists of list of points
image, contours, hierarchy = cv2.findContours(CannyEdge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# check here -
#print contours




# Draw Contour
cv2.drawContours(image,contours,-1,(0,255,0),5)

cv2.imshow("Contour Image" , image)
cv2.waitKey()

cv2.destroyAllWindows()