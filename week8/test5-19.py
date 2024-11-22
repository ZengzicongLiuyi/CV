#test5-19.py：霍夫圆
import cv2
import numpy as np
img=cv2.imread('shape6.jpg')                				#读取图像
cv2.imshow('original',img)  	            			#显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   			#转化为灰度图像
edges=cv2.Canny(gray,50,150,apertureSize =3)         #执行边缘检测
circles= cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,50,
                            param2=30,minRadius=10,maxRadius=40)#检测圆
circles = np.uint16(np.around(circles))
print("circles",circles)
img2=img.copy()
for i in circles[0,:]:
    cv2.circle(img2,(i[0],i[1]),i[2],(255,0,0),2)           #画圆
    cv2.circle(img2,(i[0],i[1]),2,(0,0,255),3)              #画圆心
cv2.imshow('circles',img2)  	                  	    	#显示结果图像
cv2.waitKey(0)                                      		#按任意键结束等待
cv2.destroyAllWindows()                             		#关闭所有窗口
