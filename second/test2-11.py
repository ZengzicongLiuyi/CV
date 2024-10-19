#test2-11.py：使用cv2.split()函数拆分通道
import cv2
img=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_COLOR_2)  	#读取图像，缩小为原来的1/2
cv2.imshow('lena',img)          #显示原图像
b,g,r=cv2.split(img)            #按通道拆分图像
cv2.imshow('lena_B',b)          #显示B通道图像
cv2.imshow('lena_G',g)          #显示G通道图像
cv2.imshow('lena_R',r)          #显示R通道图像
cv2.waitKey(0)