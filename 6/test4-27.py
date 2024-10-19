#test4-27.py：膨胀
import cv2
import numpy as np
img=cv2.imread('zh.jpg')                  #读取图像
cv2.imshow('img',img)                       #显示原图像
kernel = np.ones((5,5),np.uint8)            #定义5×5核心
img2 = cv2.dilate(img,kernel,iterations = 2) #膨胀，迭代5次
cv2.imshow('img2',img2)                     #显示转换结果图像
cv2.waitKey(0)