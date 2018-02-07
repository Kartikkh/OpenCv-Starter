import numpy as np
import cv2



image = cv2.imread('image.jpg')
cv2.imshow("Original" ,  image)
cv2.waitKey()


gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# goodFeaturesToTrack  takes params
# 1 gray image
# 2 No. of corner to find
# 3 Quality of corner
# 4 Distance between each corner

corners = cv2.goodFeaturesToTrack(gray,100,0.01,5)
print corners



for i in corners:
    x, y = i.ravel()
    cv2.circle(image, (x, y), 3, 255, -1)

cv2.imshow("TargetOutput",image)

cv2.waitKey()
cv2.destroyAllWindows()


