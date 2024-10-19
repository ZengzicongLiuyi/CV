import numpy as np
import cv2
img = np.zeros((400,400,3),np.uint8)
cv2.line(img,(50,50),(250,50),(255,0,0),10)
cv2.line(img,(50,50),(125,250),(255,0,0),10)
cv2.line(img,(250,50),(125,250),(255,0,0),10)
cv2.imshow('draw',img)
cv2.waitKey(0)