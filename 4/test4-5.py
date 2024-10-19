#test4-5.py：缩放图像
import cv2
img=cv2.imread('bee.jpg')  	#读取图像
sc=[1,0.2,0.5,1.5,2]            #设置缩放比例
cv2.imshow('showimg',img)  	#显示图像
while True:                   	    
    key=cv2.waitKey()
    if 48<=key<=52: #按键【0】、【1】、【2】、【3】或【4】
        x=y=sc[key-48]  #获得缩放比例
        img2=cv2.resize(img,None,fx=x,fy=y)   #缩放图像
        cv2.imshow('showimg',img2)  	        #显示图像
