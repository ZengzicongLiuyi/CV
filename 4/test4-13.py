#test4-13.py：高斯滤波
import cv2
img=cv2.imread('lena2.jpg')
cv2.imshow('img',img) 
img2=cv2.GaussianBlur(img,(51,51),0,0)#可调整卷积核大小查看不同效果
cv2.imshow('imgBlur',img2)
cv2.waitKey(0)