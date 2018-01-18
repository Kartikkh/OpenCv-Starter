import numpy as np
import cv2

## Open CV stores value in BRG format


# For Loading Images use imread('Name of Image')
# open CV creates a image array and store all the information
image = cv2.imread('image.jpg')
# For Showing Image by this HelloWorld Name
cv2.imshow('helloWorld' , image)

# Getting Color values from the array
B ,G ,R  = cv2.split(image)
print B, G, R
cv2.imshow("Red" , R)
cv2.imshow("Blue" , B)
cv2.imshow("Green" , G)



cv2.waitKey()

cv2.destroyAllWindows()


