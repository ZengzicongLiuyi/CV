#test4-20.py：截断阈值处理
import cv2
img=cv2.imread('bee.jpg')
cv2.imshow('img',img)
ret,img2=cv2.threshold(img,150,255,cv2.THRESH_TRUNC)#阈值处理
cv2.imshow('imgTHRESH_TRUNC',img2)
cv2.waitKey(0)