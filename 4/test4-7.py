#test4-7.py：图像向左移动100像素，向下移动50像素
import cv2
import numpy as np
img=cv2.imread('bee.jpg')  	#读取图像
cv2.imshow('img',img)  	        #显示图像
height=img.shape[0]             #获得图像高度
width=img.shape[1]#获得图像宽度
dsize=(width,height)
m=np.float32([[1,0,100],[0,1,50]])#创建转换矩阵
img2=cv2.warpAffine(img,m,dsize)        #平移图像
cv2.imshow('imgx+100y+50',img2)  	#显示图像
cv2.waitKey(0)
