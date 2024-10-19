#test4-9.py：图像旋转
import cv2
img=cv2.imread('bee.jpg')  	#读取图像
cv2.imshow('img',img)  	        #显示图像
height=img.shape[0]             #获得图像高度
width=img.shape[1]              #获得图像宽度
dsize=(width,height)
m=cv2.getRotationMatrix2D((width/2,height/2), -60, 0.5)#创建转换矩阵
img2=cv2.warpAffine(img,m,dsize)        #执行旋转
cv2.imshow('imgRotation',img2)  	#显示图像
cv2.waitKey(0)