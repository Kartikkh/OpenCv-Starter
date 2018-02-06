import cv2
import numpy as np
#
# For Reference
# https://www.learnopencv.com/blob-detection-using-opencv-python-c/
# A blob is group of connected pixel that shares same property in a binary image

Sunflower =  cv2.imread('blob.jpg',cv2.IMREAD_GRAYSCALE)

# Setup the detector
detector = cv2.SimpleBlobDetector_create()


# Detect the image

points = detector.detect(Sunflower)

blank= np.zeros((1,1))
blob = cv2.drawKeypoints(Sunflower,points,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("BlobOutput",blob)


cv2.waitKey()
cv2.destroyAllWindows()



