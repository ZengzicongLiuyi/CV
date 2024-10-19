#test2-14.py：图像的加权加法运算
import cv2
img1=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_COLOR_2)  	#读取图像
img2=cv2.imread('opencvlog.jpg',cv2.IMREAD_REDUCED_COLOR_2)	#读取图像
img3=cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('lena',img1)          		#显示原图像
cv2.imshow('log',img2)          		#显示原图像
cv2.imshow('lena+log',img3)         	#显示addWeighted()图像
cv2.waitKey(0)
