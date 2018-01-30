import cv2

Orgimage = cv2.imread('image.jpg')


grayimage = cv2.cvtColor(Orgimage, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimage" ,  grayimage)
cv2.waitKey()



CannyEdge = cv2.Canny(grayimage,50,100)
cv2.imshow("CannyEdges" ,  CannyEdge)
cv2.waitKey()

image, contours, hierarchy = cv2.findContours(CannyEdge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


# cv2.drawContours(image,contours,-1,(0,255,0),5)
#
# cv2.imshow("Contour Image" , image)
# cv2.waitKey()

def contour_Area (contours):
  area =[]

  for c in contours :
      C_area = cv2.contourArea(c)
      area.append(C_area)

  return area


Sorted_Contour = sorted(contours,key=cv2.contourArea,reverse=True)

print Sorted_Contour



for c in Sorted_Contour :
    cv2.drawContours(Orgimage,[c],-1,(0,0,255),5)
    cv2.waitKey(0)
    cv2.imshow("Contour By Area",Orgimage)


cv2.destroyAllWindows()

