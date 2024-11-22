#test7-3.py：距离转换
import cv2
import numpy as np
img=cv2.imread('coins.jpg')
cv2.imshow('original',img)      #显示原图
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度图
ret,imgthresh=cv2.threshold(gray,0,255,
            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)#Otsu阈值处理
kernel=np.ones((3,3),np.uint8)#定义形态变换卷积核
imgopen=cv2.morphologyEx(imgthresh,cv2.MORPH_OPEN,
                                kernel,iterations=2)#形态变换：开运算
imgdist=cv2.distanceTransform(imgopen,cv2.DIST_L2,5)#距离转换
cv2.imshow('distance',imgdist)#显示距离转换结果
cv2.waitKey(0)