import cv2
import numpy as np
#https://www.geeksforgeeks.org/erosion-dilation-images-using-opencv-python/
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

img = cv2.imread('image.jpg')
kernel = np.ones((5,5),np.uint8)


#Erosion
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow("erosion",erosion)
cv2.waitKey(0)

cv2.destroyAllWindows()

#Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("dilation",dilation)
cv2.waitKey(0)

cv2.destroyAllWindows()


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening",opening)
cv2.waitKey(0)

cv2.destroyAllWindows()



closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing",closing)
cv2.waitKey(0)

cv2.destroyAllWindows()

