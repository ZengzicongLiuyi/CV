#test4-22.py：低阈值零处理
import cv2
img=cv2.imread('bee.jpg')
cv2.imshow('img',img)
ret,img2=cv2.threshold(img,150,255,cv2.THRESH_TOZERO)#阈值处理
cv2.imshow('imgTHRESH_TOZERO',img2)
cv2.waitKey(0)