import numpy as np
import cv2

# Sharping is opposite of blurring, It strengthen the edges of an image

img = cv2.imread('image.jpg')

kernel_3 = np.array([
                        [-1,-1,-1],
                        [-1,9,-1],
                        [-1,-1,-1]
                    ])

sharpImage = cv2.filter2D(img,-1,kernel_3)

cv2.imshow("sharpImage",sharpImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

