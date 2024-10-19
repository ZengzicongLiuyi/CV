#test2-13.py：图像加法运算
import cv2
img1=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_COLOR_2)  	#读取图像
img2=cv2.imread('opencvlog.jpg',cv2.IMREAD_REDUCED_COLOR_2)	#读取图像
img3=img1+img2
img4=cv2.add(img1,img2)
cv2.imshow('lena',img1)          		#显示原图像
cv2.imshow('log',img2)          		#显示原图像
cv2.imshow('lena+log',img3)         	#显示“+”图像
cv2.imshow('lenaaddlog',img4)     		#显示add()图像
cv2.waitKey(0)