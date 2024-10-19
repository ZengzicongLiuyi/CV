#test4-19.py：反二值化阈值处理
import cv2
img=cv2.imread('bee.jpg')
cv2.imshow('img',img)
ret,img2=cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)#阈值处理
cv2.imshow('imgTHRESH_BINARY_INV',img2)
cv2.waitKey(0)