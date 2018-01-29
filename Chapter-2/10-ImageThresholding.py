#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

import cv2


img = cv2.imread('image.jpg',0)

#Simple Thresholding
#Here, the matter is straight forward. If pixel value is greater than a threshold value, it is assigned one value (may be white),
# else it is assigned another value (may be black). The function used is cv2.threshold.
# First argument is the source image, which should be a gray scale image.
# Second argument is the threshold value which is used to classify the pixel values.
#  Third argument is the maxVal which represents the value to be given if pixel value is more than
#  (sometimes less than) the threshold value.

#  OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. Different types are:
# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("thresh1",thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()


ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thresh2",thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()


ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv2.imshow("thresh3",thresh3)
cv2.waitKey(0)
cv2.destroyAllWindows()




ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow("thresh4",thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()



ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("thresh5",thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()


