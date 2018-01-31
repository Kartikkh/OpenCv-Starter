import cv2

#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html

#read both the images
ShapesImage =  cv2.imread('image.jpg',0)
StarImage = cv2.imread('star.jpg',0)


ret,Shapethresh = cv2.threshold(ShapesImage,127,255,cv2.THRESH_BINARY_INV)
ret,Starthresh = cv2.threshold(StarImage,127,255,cv2.THRESH_BINARY_INV)


image1,Shapecontours, Shapehierarchy = cv2.findContours(Shapethresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


imag2,Starcontours, Starhierarchy = cv2.findContours(Starthresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# Finding The Largest Contour in the Matched Image
Starcnt = Starcontours[0]



# looping in order to find which image matches in the Target Matched Image
#MatchShapes function return the match value contain the upto how much Percentage of image matched


for c in Shapecontours:
    match = cv2.matchShapes(c, Starcnt, 1, 0.0)
    print match
    if match <0.5:
        closest_contour = c
    else:
        closest_contour = []


cv2.drawContours(StarImage,[closest_contour],-1,(0,0,150),3)
cv2.imshow("TargetOutput",StarImage)


cv2.waitKey()
cv2.destroyAllWindows()


