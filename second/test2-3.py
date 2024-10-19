#test2-3.py：显示图像
import cv2
img=cv2.imread('lena.jpg')  	#读取图像，缩小为原来的1/2
cv2.imshow('lena',img)          #显示图像
cv2.waitKey()

