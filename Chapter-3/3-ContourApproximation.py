import numpy as np
import cv2

Orgimage = cv2.imread('house.jpg')
ApproxImage = Orgimage.copy()

grayimage = cv2.cvtColor(Orgimage, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimage" ,  grayimage)
cv2.waitKey()

ret,thresh = cv2.threshold(grayimage,127,255,cv2.THRESH_BINARY_INV)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# boundRect function returns the point of top left and width and height of contour
# here we use that points to create a rectangle

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(Orgimage,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("Bounding Rectangle" , Orgimage )

cv2.waitKey()


for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(Orgimage,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("Bounding Rectangle" , Orgimage )


# Contour Approximation
# since we are not getting a exact square in the image so here we can use contour Approximations
for c in contours:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    cv2.drawContours(ApproxImage,[approx],0,(0,0,255),3)
    cv2.imshow("Approximation", ApproxImage)


cv2.waitKey()





cv2.destroyAllWindows()