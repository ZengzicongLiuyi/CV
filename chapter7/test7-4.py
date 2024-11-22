#test7-4.py：使用分水岭算法分割图像
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('qizi.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)           #转换为灰度图
ret,imgthresh=cv2.threshold(gray,0,255,
            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #Otsu阈值处理
kernel=np.ones((3,3),np.uint8)                      #定义形态变换卷积核
imgopen=cv2.morphologyEx(imgthresh,cv2.MORPH_OPEN,
            kernel,iterations=2)                    #形态变换：开运算
imgbg=cv2.dilate(imgopen,kernel,iterations=3)       #膨胀操作，确定背景
imgdist=cv2.distanceTransform(imgopen,cv2.DIST_L2,0)#距离转换
ret,imgfg=cv2.threshold(imgdist,
                    0.7*imgdist.max(),255,2)#对距离转换结果进行阈值处理
imgfg=np.uint8(imgfg)                       #转换为整数，获得前景
ret,markers=cv2.connectedComponents(imgfg)  #标记阈值处理结果
unknown=cv2.subtract(imgbg,imgfg)           #确定位置未知区域
markers=markers+1                           #加1使背景不为0
markers[unknown==255]=0                     #将未知区域设置为0
imgwater=cv2.watershed(img,markers)         #执行分水岭算法分割图像
plt.imshow(imgwater)                  		#以灰度图像格式显示匹配结果
plt.title('watershed')
plt.axis('off') 
plt.show()           
img[imgwater==-1]=[0,255,0]          #将原图中被标记点设置为绿色
cv2.imshow('watershed',img)         #显示分割结果
cv2.waitKey(0)
