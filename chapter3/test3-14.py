import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8) 
cv2.rectangle(img,(20,20),(300,180),(255,0,0),10)
cv2.rectangle(img,(70,70),(250,130),(0,255,0),2)
cv2.imshow('draw',img)
cv2.waitKey(0)