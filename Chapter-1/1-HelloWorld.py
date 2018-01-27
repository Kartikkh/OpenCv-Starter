import cv2

## Open CV stores value in BRG format

# For Loading Images use imread('Name of Image')
image = cv2.imread('image.jpg')
# For Showing Image by this HelloWorld Name
cv2.imshow('helloWorld' , image)

# This will allow you to input information when image window is open
# by leaving it blank it just wait for anykey to be pressed before continuing
## we can place argument (except 0 for 0 it will wait forever to exit for key press ) we can specify the delay ,
#  how long to keep the window open
cv2.waitKey()

# this close all the open windows
# failure of this will make the program in hung state
cv2.destroyAllWindows()
