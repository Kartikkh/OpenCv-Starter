import cv2

#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html

OrgImage =  cv2.imread('hand.jpg',0)


ret,thresh = cv2.threshold(OrgImage,127,255,cv2.THRESH_BINARY_INV)


image, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print contours


for c in contours:
    #print c
    hull = cv2.convexHull(c)
    print hull
    cv2.drawContours(OrgImage,[hull],0,(0,0,255),3)
    cv2.imshow("ConvexHull Image" , OrgImage)

cv2.waitKey()
cv2.destroyAllWindows()
