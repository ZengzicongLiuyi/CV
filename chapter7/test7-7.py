#test7-7.py：拉普拉斯金字塔
import cv2
img0=cv2.imread('qizi.jpg')
img1=cv2.pyrDown(img0)          #第1次采样
img2=cv2.pyrDown(img1)          #第2次采样
img3=cv2.pyrDown(img2)          #第3次采样
imgL0= cv2.subtract( img0,cv2.pyrUp(img1))     #拉普拉斯金字塔第0层
imgL1= cv2.subtract(img1,cv2.pyrUp(img2) )     #拉普拉斯金字塔第1层
imgL2= cv2.subtract(img2,cv2.pyrUp(img3) )     #拉普拉斯金字塔第2层
cv2.imshow('imgL0',img0)       #显示第0层
cv2.imshow('imgL1',img1)       #显示第1层
cv2.imshow('imgL2',img2)       #显示第2层
cv2.waitKey(0)
