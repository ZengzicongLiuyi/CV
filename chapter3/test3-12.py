import numpy as np
import cv2
img = np.zeros((120,400,3),np.uint8)
def dochange(x):
    b=cv2.getTrackbarPos('B','trakbar')
    g=cv2.getTrackbarPos('G',"trakbar")
    r=cv2.getTrackbarPos('R',"trakbar")
    img[:]=[b,g,r]
cv2.namedWindow('trakbar')
cv2.createTrackbar('B','trakbar',0,255,dochange)
cv2.createTrackbar('G','trakbar',0,255,dochange)
cv2.createTrackbar('R','trakbar',0,255,dochange)
while(True):
    cv2.imshow('trakbar',img)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()