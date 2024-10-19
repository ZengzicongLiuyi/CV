#test3-5.py：绘制圆
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8) #创建一幅黑色图像
cv2.circle(img,(160,100),80,(255,0,0),5)#画圆，蓝色边框
cv2.circle(img,(160,100),40,(0,255,0),-1)#画圆，绿色填充
cv2.imshow('draw',img)          #显示图像
cv2.waitKey(0)