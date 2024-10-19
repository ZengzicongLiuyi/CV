#test4-18.py：二值化阈值处理
import cv2
img=cv2.imread(r'D:\cv\6\mango.jpg')
cv2.imshow('img',img)
ret,img2=cv2.threshold(img,150,255,cv2.THRESH_BINARY)#阈值处理
print("ret:", ret)
cv2.imshow('imgTHRESH_BINARY',img2)
cv2.waitKey(0)