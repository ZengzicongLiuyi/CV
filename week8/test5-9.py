#test5-9.py：轮廓的近似多边形
import cv2
import numpy as np
img=cv2.imread('shape3.jpg')        #读取图像
cv2.imshow('original',img)  	    #显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图像
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)#二值化阈值处理
c,h=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
ep=[0.1,0.05,0.01]
arcl=cv2.arcLength(c[0],True)                  #计算轮廓长度
print(arcl)
img3=np.zeros(img.shape, np.uint8)+255 	        #按原图大小创建一幅白色图像
img3=cv2.drawContours(img3,c,-1,(0,0,255),2)    #绘制轮廓
for n in range(3):
    eps=ep[n]*arcl
    img4=img3.copy()
    app=cv2.approxPolyDP(c[0],eps,True)         #获得近似多边形
    img4=cv2.drawContours(img4,[app],-1,(255,0,0),2)    #绘制近似轮廓
    cv2.imshow('appro %.2f' % ep[n],img4)  	                #显示轮廓图像
cv2.waitKey(0)                                  #按任意键结束等待
cv2.destroyAllWindows()                         #关闭所有窗口