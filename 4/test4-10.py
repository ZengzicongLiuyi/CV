
import cv2
import numpy as np
img=cv2.imread('bee.jpg')  	#读取图像
cv2.imshow('img',img)  	        #显示图像
height=img.shape[0]             #获得图像高度
width=img.shape[1]              #获得图像宽度
dsize=(width,height)
src=np.float32([[0,0],[width-10,0],[0,height-1]])#取原图像中三个点
dst=np.float32([[50,50],[width-100,80],[100,height-100]])#设置三点在目标图像中的坐标
m = cv2.getAffineTransform(src, dst)#创建转换矩阵
img2=cv2.warpAffine(img,m,dsize)        #执行转换
cv2.imshow('imgThreePoint',img2)  	#显示图像
cv2.waitKey(0)