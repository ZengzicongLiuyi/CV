#test4-16.py：双边滤波
import numpy as np
import cv2
img=cv2.imread('lena2.jpg')
cv2.imshow('img',img) 
img2=cv2.bilateralFilter(img,50,50,50)#可调整参数查看不同效果
cv2.imshow('imgBlur',img2)
cv2.waitKey(0)