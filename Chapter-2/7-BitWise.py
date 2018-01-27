import cv2
import numpy as np


# create a black Image
rectangle = np.zeros((300,300),np.uint8)


# Draw Rectangle
cv2.rectangle(rectangle,(50,50),(250,250),255,-2)

cv2.imshow("Rectangle",rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw Eclipse
# create a black Image
eclipse = np.zeros((300,300),np.uint8)
cv2.ellipse(eclipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("Eclipse",eclipse)
cv2.waitKey(0)
cv2.destroyAllWindows()


And = cv2.bitwise_and(rectangle,eclipse)
cv2.imshow("And",And)
cv2.waitKey(0)
cv2.destroyAllWindows()


OR = cv2.bitwise_or(rectangle,eclipse)
cv2.imshow("OR",OR)
cv2.waitKey(0)
cv2.destroyAllWindows()

Not = cv2.bitwise_not(rectangle,eclipse)
cv2.imshow("Not",Not)
cv2.waitKey(0)
cv2.destroyAllWindows()

XOR = cv2.bitwise_xor(rectangle,eclipse)
cv2.imshow("XOR",XOR)
cv2.waitKey(0)
cv2.destroyAllWindows()
