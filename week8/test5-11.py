#test5-11.py：轮廓的直边界矩形
import cv2
import numpy as np
img=cv2.imread('shape4.jpg')                			#读取图像
cv2.imshow('original',img)  	            			#显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   			#转化为灰度图像
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)	#二值化阈值处理
c,h=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #计算轮廓
img3=np.zeros(img.shape, np.uint8)+255 	        	    #按原图大小创建一幅白色图像
cv2.drawContours(img3,c,-1,(0,0,255),2)         		#绘制轮廓
ret=cv2.boundingRect(c[0])                      		#计算直边矩形
print('直边界矩形：',ret)
pt1=(ret[0],ret[1])
pt2=(ret[0]+ret[2],ret[1]+ret[3])
cv2.rectangle(img3,pt1,pt2,(255,0,0),2)             	#绘制直边界矩形
cv2.imshow('Rectangle',img3)  	                  	    #显示结果图像
cv2.waitKey(0)                                      	#按任意键结束等待
cv2.destroyAllWindows()                             	#关闭所有窗口
