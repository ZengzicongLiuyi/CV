#test4-6.py：翻转图像
import cv2
img=cv2.imread('bee.jpg')  	#读取图像
cv2.imshow('showimg',img)  	#显示图像
while True:                   	    
    key=cv2.waitKey()
    if key==48:                 #按【0】键时显示原图 
        img2=img
    elif key==49:               #按【1】键时垂直翻转
        img2=cv2.flip(img,0)
    elif key==50:               #按【2】键时水平翻转
        img2=cv2.flip(img,1)
    elif key==51:               #按【3】键时水平、垂直翻转
        img2=cv2.flip(img,-1)
    cv2.imshow('showimg',img2)
