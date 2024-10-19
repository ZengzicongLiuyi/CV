#test4-4.py：BGR色彩空间转换为HSV色彩空间
import cv2
img=cv2.imread('bee.jpg')  	#读取图像
cv2.imshow('BGR',img)  	        #显示图像
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #转换色彩空间为HSV
cv2.imshow('HSV',img2)  	        #显示图像
cv2.waitKey(0)