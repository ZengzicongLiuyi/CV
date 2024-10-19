#test4-24.py：三角算法阈值处理
import cv2
img=cv2.imread('bee.jpg',cv2.IMREAD_GRAYSCALE)#读取图像，转化为单通道灰度图像
cv2.imshow('img',img)#显示原图
ret,img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#阈值处理
cv2.imshow('img2',img2)
ret,img3=cv2.threshold(img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('img3',img3)
ret,img4=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_TRIANGLE)
cv2.imshow('img4',img4)
cv2.waitKey(0)
