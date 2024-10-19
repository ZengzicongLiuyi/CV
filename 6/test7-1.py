import cv2
import numpy as np
img = cv2.imread(r'D:\cv\6\bee2.bmp')
cv2.imshow('original',img)
img2 = cv2.Canny(img,100,150)
cv2.imshow('Canny',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()