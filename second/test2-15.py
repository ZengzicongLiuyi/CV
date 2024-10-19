#test2-15.py：图像位运算
import cv2
src1=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_COLOR_2)  	#读取图像
src2=cv2.imread('opencvlog.jpg',cv2.IMREAD_REDUCED_COLOR_2)	#读取图像
img3=cv2.bitwise_and(src1,src2)#按位与
img4=cv2.bitwise_or(src1,src2)#按位或
img5=cv2.bitwise_not(src1)#按位取反
img6=cv2.bitwise_xor(src1,src2)#按位异或                     
cv2.imshow('lena',src1)          		#显示原图像
cv2.imshow('log',src2)          		#显示原图像
cv2.imshow('lenaandlog',img3)         		#显示按位与图像
cv2.imshow('lenaorlog',img4)         		#显示按位或图像
cv2.imshow('lenanotlog',img5)         		#显示按位取反图像
cv2.imshow('lenaxorlog',img6)         		#显示按位异或图像
cv2.waitKey(0)