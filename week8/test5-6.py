#test5-6.py：轮廓矩
import cv2
import numpy as np
img=cv2.imread(r'gate.jpg')        #读取图像
cv2.imshow('original',img)  	    #显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图像
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)#二值化阈值处理
c,h=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
img3=np.zeros(img.shape, np.uint8)+255 	    #按原图大小创建一幅白色图像
img3=cv2.drawContours(img3,c,-1,(0,0,255),2)    #绘制轮廓
cv2.imshow('Contours',img3)  	                #显示轮廓图像
for n in range(len(c)):
    m=cv2.moments(c[n])
    print('轮廓%s的矩：'%n,m)   #输出轮廓矩
    print('轮廓%s的面积：'%n,m['m00'])   #输出轮廓面积
cv2.waitKey(0)                                  #按任意键结束等待
cv2.destroyAllWindows()                         #关闭所有窗口