#test5-17.py：霍夫直线
import cv2
import numpy as np
img=cv2.imread('shape6.jpg')                				#读取图像
cv2.imshow('original',img)  	            			#显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   			#转化为灰度图像
edges = cv2.Canny(gray,50,150,apertureSize =3)         #执行边缘检测
lines=cv2.HoughLines(edges,1,np.pi/180,200)             #霍夫线变换
print("lines",lines)
img3=img.copy()
for line in lines:                                      #逐条绘制直线
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0, y0 = a*rho, b*rho
    pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )#计算直线端点
    pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )#计算直线端点
    cv2.line(img3, pt1, pt2, (0, 0,255), 2)#绘制直线
cv2.imshow('HoughLines',img3)  	                  	    	#显示结果图像
cv2.waitKey(0)                                      		#按任意键结束等待
cv2.destroyAllWindows()                             		#关闭所有窗口
