

import cv2


# Pyramiding image refers to either Up scaling or Downscaling the image
# Alternate method to resize It scale or resize the image to 50%

image = cv2.imread('image.jpg')
smaller = cv2.pyrDown(image)
# Getting back the original image, But it will be somewhat blurry compared to original image
larger   = cv2.pyrUp(image)

cv2.imshow("original", image)
cv2.waitKey()
cv2.imshow("smaller " ,smaller)
cv2.waitKey()
cv2.imshow("larger " ,larger)
cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()