#test7-6.py：高斯金字塔向上采样
import cv2
img0=cv2.imread(r'D:\cv\chapter7\qizi2.jpg')
img1=cv2.pyrUp(img0)          #第1次采样
img2=cv2.pyrUp(img1)          #第2次采样
cv2.imshow('img0',img0)       #显示第0层
cv2.imshow('img1',img1)       #显示第1层
cv2.imshow('img2',img2)       #显示第2层
print('0层形状：',img0.shape)             #输出图像形状
print('1层形状：',img1.shape)             #输出图像形状
print('2层形状：',img2.shape)             #输出图像形状
cv2.waitKey(0)
