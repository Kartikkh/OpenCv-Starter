import cv2

# Adaptive Thresholding
# In simple thresholding mechanism we put the Threshold value which is not good because sometimes we don't know much about image
# But it may not be good in all the conditions where image has different lighting conditions in different areas
# so in Adaptive thresholding we calculate the threshold for a small regions of the image. So we get different thresholds for
# different regions of the same image and it gives us better results for images with varying illumination.

img = cv2.imread('image.jpg',0)


th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,7)
cv2.imshow("th2",th2)
cv2.waitKey(0)




th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()



