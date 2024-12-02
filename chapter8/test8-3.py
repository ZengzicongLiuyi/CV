#test8-3.py：Shi-Tomasi角检测
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('bridge.jpg')                    #打开图像，默认BGR格式
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #转换为灰度图像
gray = np.float32(gray)                         #转换为浮点类型
corners = cv2.goodFeaturesToTrack(gray,20,0.1,100)#检测角，最多20个
corners = np.int0(corners)                          #转换为整型
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),4,(0,0,255),-1)        #用圆点标注找到的角，红色
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)       #转换为RGB格式
plt.imshow(img)
plt.axis('off')
plt.show()                                      #显示检测结果