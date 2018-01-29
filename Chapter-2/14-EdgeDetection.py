import cv2

# Edge is defined as a sudden change in Image in term of Intensity
# Main Type of Edge Detection Algorithms
# Laplacian
# Canny
# Sobel

img = cv2.imread('image.jpg',0)

height , width = img.shape

# Sobel Edge Detection
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

cv2.imshow("SobelX",sobelx)
cv2.waitKey(0)
cv2.imshow("Soble_y",sobely)
cv2.waitKey(0)

SobelFullImage = cv2.bitwise_or(sobelx,sobely)
cv2.imshow("SobleFullImage",SobelFullImage)
cv2.waitKey(0)


# Laplacian Edge Detection
LaplacianImage = cv2.Laplacian(img,cv2.cv2.CV_64F)
cv2.imshow("LaplacianImage",LaplacianImage)
cv2.waitKey(0)

# Canny Edge Detection
# Value below threshold (100) here is not consider to be edge and value above threshold (200) here is consider as an edge
CannyImage = cv2.Canny(img,100,200)
cv2.imshow("CannyImage",CannyImage)
cv2.waitKey(0)


cv2.destroyAllWindows()




