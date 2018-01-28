
## Blurring is a operation where we average the pixel with that region
#In image processing, a kernel, convolution matrix, or mask is a small matrix. It is used for blurring, sharpening,
#embossing, edge detection, and more.
#This is accomplished by doing a convolution between a kernel and an image.

#  https://www.youtube.com/watch?v=C_zFhWdM4ic&t=301s
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html


import cv2
import numpy as np


image = cv2.imread('image.jpg')

cv2.imshow('Original Image' , image)

cv2.waitKey(0)

kernel_3 = np.ones((3,3),np.float32)/9

blurImage = cv2.filter2D(image,-1,kernel_3)

cv2.imshow("blurredImage",blurImage)

cv2.waitKey(0)
cv2.destroyAllWindows()


# checking with kernel of different size


kernel_9 = np.ones((20,20),np.float32)/400
blurImage = cv2.filter2D(image,-1,kernel_3)

cv2.imshow("blurredImage",blurImage)

cv2.waitKey(0)
cv2.destroyAllWindows()


## Other Blur Techniques

# Averaging
#This is done by convolving the image with a normalized box filter. It simply takes the average of all the pixels under kernel area
# and replaces the central element with this average. This is done by the function cv2.blur() or cv2.boxFilter().
img = cv2.imread('image.jpg')
blur = cv2.blur(img,(5,5))
cv2.imshow("blur",blur)
cv2.waitKey(0)


#Gaussian Filtering
#In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used.
# It is done with the function, cv2.GaussianBlur().
# We should specify the width and height of the kernel which should be positive and odd.

img = cv2.imread('image.jpg')
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("blur",blur)
cv2.waitKey(0)


# Median Filtering
# Here, the function cv2.medianBlur() computes the median of all the pixels under the kernel window and the central pixel
#  is replaced with this median value. This is highly effective in removing salt-and-pepper noise.
# One interesting thing to note is that, in the Gaussian and box filters, the filtered value for the central element
# can be a value which may not exist in the original image. However this is not the case in median filtering,
#  since the central element is always replaced by some pixel value in the image. This reduces the noise effectively.
# The kernel size must be a positive odd integer.

img = cv2.imread('image.jpg')
median = cv2.medianBlur(img,5)
cv2.imshow("median",median)
cv2.waitKey(0)

#Bilateral Filtering
#bilateral filter, cv2.bilateralFilter(), which was defined for, and is highly effective at noise removal while preserving edges.

img = cv2.imread('image.jpg')
bilateralFilter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateralFilter",bilateralFilter)
cv2.waitKey(0)



cv2.destroyAllWindows()
