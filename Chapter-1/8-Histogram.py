import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('image.jpg')

## For Extra Resources https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html



# we can directly use MatplotLib to directly plot Histogram
plt.hist(image.ravel(),256,[0,256])
plt.show()

## OR


     #cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#hist = cv2.calcHist([image],[0],None,[256],[0,256])

# So now we use cv2.calcHist() function to find the histogram. Let's familiarize with the function and its parameters :
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
# channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
# mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
# histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
# ranges : this is our RANGE. Normally, it is [0,256].

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.show()