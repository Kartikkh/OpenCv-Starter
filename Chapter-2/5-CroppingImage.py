import cv2


image = cv2.imread('image.jpg')
height , width = image.shape[:2]


start_Row , start_Col = int( 0.25 *height) , int( 0.25 *width)

end_Row , end_Col = int( 0.75 *height) , int( 0.75 *width)

cropped = image[start_Row : end_Row ,start_Col: end_Col]

cv2.imshow("Original Image" ,image)

cv2.imshow("Cropped ",cropped)


cv2.waitKey()
cv2.destroyAllWindows()