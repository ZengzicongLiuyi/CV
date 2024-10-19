#test4-8.py：图像缩放
import cv2
import numpy as np
img=cv2.imread('bee.jpg')  	#读取图像
cv2.imshow('img',img)  	        #显示图像
height=img.shape[0]             #获得图像高度
width=img.shape[1]              #获得图像宽度
dsize=(width,height)
m=np.float32([[0.5,0,0],[0,0.5,0]])#创建转换矩阵
img2=cv2.warpAffine(img,m,dsize)        #执行缩放
cv2.imshow('img0.5x+0.5y',img2)  	#显示图像
cv2.waitKey(0)