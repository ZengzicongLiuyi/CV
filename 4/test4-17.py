#test4-17.py：2D卷积
import numpy as np
import cv2
img=cv2.imread('lena2.jpg')
k1=np.array([[3,3,3,3,3],
             [3,9,9,9,3],
             [3,11,12,13,3],
             [3,8,8,8,3],
             [3,3,3,3,3],])/25#自定义卷积核1
k2=np.ones((5,5),np.float32)/25#自定义卷积核2
img2=cv2.filter2D(img,-1,k1)
cv2.imshow('imgK1',img2)
img2=cv2.filter2D(img,-1,k2)
cv2.imshow('imgK2',img2)
cv2.waitKey(0)