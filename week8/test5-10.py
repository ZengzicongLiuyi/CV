#test5-10.py：轮廓的凸包
import cv2
import numpy as np
img=cv2.imread('shape3.jpg')        #读取图像
cv2.imshow('original',img)  	    #显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图像
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)#二值化阈值处理
c,h=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #计算轮廓
img3=np.zeros(img.shape, np.uint8)+255 	        #按原图大小创建一幅白色图像
img3=cv2.drawContours(img3,c,-1,(0,0,255),2)    #绘制轮廓
hull = cv2.convexHull(c[0])
print('returnPoints=True时返回的凸包：\n',hull)
hull2 = cv2.convexHull(c[0],returnPoints=False)
print('returnPoints=False时返回的凸包：\n',hull2)
cv2.polylines(img3,[hull],True,(255,0,0),2)	        #绘制凸包
cv2.imshow('Convex Hull',img3)  	                #显示轮廓图像
cv2.waitKey(0)                                      #按任意键结束等待
cv2.destroyAllWindows()                             #关闭所有窗口