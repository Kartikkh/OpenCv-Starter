
import matplotlib.pyplot as plt
import cv2
import numpy as np


# create a black Image
image = np.zeros((512,512,3),np.uint8)



cv2.imshow("Color" ,image)


cv2.waitKey(0)
cv2.destroyAllWindows()



# Draw a line over a Black square

cv2.line(image,(1,2),(511,511),(88,128,77),5)

cv2.imshow("Line",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Draw Rectangle
cv2.rectangle(image,(100,100),(250,250),(150,150,150),5)

cv2.imshow("Rectangle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Draw Circle

cv2.circle(image,(300,300),150,(150,152,157),5)

cv2.imshow("Circle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Text in image

cv2.putText(image,"Hello",(100,200),cv2.FONT_HERSHEY_COMPLEX,2,(150,150,150),5)
cv2.imshow("Text",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
