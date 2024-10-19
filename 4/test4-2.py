#test4-2.py：BGR色彩空间转换为GRAY色彩空间
import cv2
img=cv2.imread('bee.jpg')  	#读取图像
cv2.imshow('BGR',img)  	        #显示图像
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #转换色彩空间为GRAY
cv2.imshow('GRAY',img2)  	        #显示图像
cv2.waitKey(0)