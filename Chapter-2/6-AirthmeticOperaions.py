import cv2
import numpy as np


image = cv2.imread('image.jpg')

# Create Matrix on image.shape with all 75

M = np.ones(image.shape ,dtype="uint8")*75

#This increase the intensity of image
# Both the parameter must have same dimensions
added  = cv2.add(image , M)
cv2.imshow("Added",added)
cv2.waitKey()
cv2.destroyAllWindows()

#This decrease the intensity of image
# Both the parameter must have same dimensions

subtract = cv2.subtract(image,M)
cv2.imshow("Subtract",subtract)

cv2.waitKey()
cv2.destroyAllWindows()