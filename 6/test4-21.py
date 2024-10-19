#test4-21.py：超阈值零处理
import cv2
img=cv2.imread('bee.jpg')
cv2.imshow('img',img)
ret,img2=cv2.threshold(img,150,255,cv2.THRESH_TOZERO_INV)#阈值处理
cv2.imshow('imgTHRESH_TOZERO_INV',img2)
cv2.waitKey(0)