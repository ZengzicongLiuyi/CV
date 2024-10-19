#test4-26.py：腐蚀
import cv2
import numpy as np
img=cv2.imread('zh2.jpg')                  #读取图像
cv2.imshow('img',img)                       #显示原图像
kernel = np.ones((5,5),np.uint8)            #定义5×5核心
img2 = cv2.erode(img,kernel,iterations = 5) #腐蚀，迭代5次
cv2.imshow('img2',img2)                     #显示转换结果图像
cv2.waitKey(0)