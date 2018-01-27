
# In case of Affine Transformation Matrix should be 2*3
##To implement this Translational we can use cv2.wrapAffine

import cv2
import numpy as np

image = cv2.imread('image.jpg')

height , width = image.shape[:2]

one_forth_Height , one_forth_Width = height/4 , width/4


T = np.float32([[1,0,one_forth_Width],[0,1,one_forth_Height]])

## wrapAffine takes 3 arguments
## image , Transformation Matrix and height and width of Original image


img_Translational = cv2.warpAffine(image,T, (width,height))



cv2.imshow("Translated Image" , img_Translational)
cv2.waitKey()
cv2.destroyAllWindows()

