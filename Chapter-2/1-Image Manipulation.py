##To implement this Translational we can use cv2.wrapAffine


import cv2
import numpy as np

image = cv2.imread('image.jpg')

height , width = image.shape[:2]

one_forth_Height , one_forth_Width = height/4 , width/4

T = np.float32([[1,0,one_forth_Width],[0,1,one_forth_Height]])

img_Traslational = cv2.warpAffine(image,T, (width,height))

cv2.imshow("Translated Image" , img_Traslational)
cv2.waitKey()
cv2.destroyAllWindows()

