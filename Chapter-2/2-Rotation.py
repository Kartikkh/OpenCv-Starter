import cv2

##Rotation
#  [

#    [ cos   - sin   ],

#      [  sin0     cos0 ]

#   ]


#cv2.getRotationMatrix( rotation_centreX , Rotation_centre_y , angel  , scale  )

image = cv2.imread('image.jpg')
height , width = image.shape[:2]

R =  cv2.getRotationMatrix2D( (width/2, height/2), 90 ,1)

RotatedImage = cv2.warpAffine(image , R , (width ,height ))

cv2.imshow("Rotated Image" ,RotatedImage)

cv2.waitKey()
cv2.destroyAllWindows()


## Another Method   (short cut)

image = cv2.imread('image.jpg')
RotatedImage =  cv2.transpose(image)
cv2.imshow("Transposed Image" ,RotatedImage)
cv2.waitKey()
cv2.destroyAllWindows()


