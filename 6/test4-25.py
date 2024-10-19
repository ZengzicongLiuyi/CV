#test4-25.py：自适应阈值处理
import cv2
img=cv2.imread('bee.jpg',cv2.IMREAD_GRAYSCALE)#读取图像，转化为单通道灰度图像
cv2.imshow('img',img)
img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY,5,10)			#阈值处理
cv2.imshow('img2',img2)
cv2.waitKey(0)