#test4-23.py：Otsu阈值处理
import cv2
img=cv2.imread('bee.jpg',cv2.IMREAD_GRAYSCALE)#读取图像，转化为单通道灰度图像
cv2.imshow('img',img)#显示原图
ret,img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#阈值处理
cv2.imshow('img2',img2)
ret1,img3=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#阈值处理
print("ret1:",ret1)
cv2.imshow('img3',img3)
ret2,img4=cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)#阈值处理
print("ret2:",ret2)
cv2.imshow('img4',img4)
cv2.waitKey(0)