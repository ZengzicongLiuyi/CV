#test5-18.py：概率霍夫直线
import cv2
import numpy as np
img=cv2.imread('shape6.jpg')                				#读取图像
cv2.imshow('original',img)  	            			#显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   			#转化为灰度图像
edges = cv2.Canny(gray,50,150,apertureSize =3)         #执行边缘检测
lines=cv2.HoughLinesP(edges,1,np.pi/180,1,
                   minLineLength=100,maxLineGap=10)             #概率霍夫线变换
print("lines",lines)
img3=img.copy()
for line in lines:                                      #逐条绘制直线
    x1,y1,x2,y2=line[0]    
    cv2.line(img3, (x1,y1), (x2,y2), (0, 0,255), 2)#绘制直线
cv2.imshow('HoughLines',img3)  	                  	    	#显示结果图像
cv2.waitKey(0)                                      		#按任意键结束等待
cv2.destroyAllWindows()                             		#关闭所有窗口
