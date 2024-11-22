#test5-15.py：轮廓的拟合直线
import cv2
import numpy as np
img=cv2.imread('shape4.jpg')                					#读取图像
cv2.imshow('original',img)  	            					#显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   					#将其转换为灰度图像
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)			#二值化阈值处理
c,h=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	#计算轮廓
img3=np.zeros(img.shape, np.uint8)+255 	        				#按原图大小创建一幅白色图像
cv2.drawContours(img3,c,-1,(0,0,255),2)         				#绘制轮廓
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(c[0], cv2.DIST_L2,0,0.01,0.01)		#计算拟合直线
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img3,(cols-1,righty),(0,lefty),(255,0,0),2)    		#绘制拟合直线
cv2.imshow('FitLine',img3)  	                  	    			#显示结果图像
cv2.waitKey(0)                                      				#按任意键结束等待
cv2.destroyAllWindows()                             				#关闭所有窗口