import numpy as np
import cv2

## Open CV stores value in BRG format


# For Loading Images use imread('Name of Image')
# open CV creates a image array and store all the information
image = cv2.imread('image.jpg')
# For Showing Image by this HelloWorld Name
cv2.imshow('helloWorld' , image)

# Getting Color values from the array
# Splitting the Image based on the color value
B ,G ,R  = cv2.split(image)
print B, G, R
cv2.imshow("Red" , R)
cv2.imshow("Blue" , B)
cv2.imshow("Green" , G)


cv2.waitKey()

cv2.destroyAllWindows()
#
#
# # MERGE Operations
# # Lets get back the original Image
merged = cv2.merge([B,G,R])
cv2.imshow("Merge Image ", merged)


cv2.waitKey()

cv2.destroyAllWindows()


# Increasing the intensity of blue color
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merge Image with Amplified Blue Color", merged)

cv2.waitKey()

cv2.destroyAllWindows()



## If you only need to filter to one color in image

B,G,R = cv2.split(image)


#print image.shape[:2]

Zero = np.zeros(image.shape[:2] ,dtype= "uint8")
print Zero

cv2.imshow("BLUE", cv2.merge([B, Zero, Zero]))
cv2.imshow("GREEN", cv2.merge([Zero, G, Zero]))
cv2.imshow("RED", cv2.merge([Zero, Zero, R]))

cv2.waitKey()

cv2.destroyAllWindows()
