import cv2

#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

#In global thresholding, we used an arbitrary value for threshold value, right? So, how can we know a value we selected is good
# or not? Answer is, trial and error method. But consider a bimodal image
#  (In simple words, bimodal image is an image whose histogram has two peaks).
# For that image, we can approximately take a value in the middle of those peaks as threshold value, right ?
#  That is what Otsu binarization does.
#  So in simple words, it automatically calculates a threshold value from image histogram for a bimodal image


img = cv2.imread('image.jpg',0)

ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("th2",th2)
cv2.waitKey(0)

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("th3",th3)
cv2.waitKey(0)

cv2.destroyAllWindows()