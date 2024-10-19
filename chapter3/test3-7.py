#test3-7.py：绘制多边形
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8)+255 #创建一幅白色图像
pts=np.array([[160,20],[20,100],[160,180],[300,100]], np.int32)#创建顶点
cv2.polylines(img,[pts],True,(255,0,0),5)#画多边形，蓝色边框
pts=np.array([[160,60],[60,100],[160,140],[260,100]], np.int32)#创建顶点
cv2.polylines(img,[pts],True,(0,255,0),1)#画曲线，绿色边框
cv2.imshow('draw',img)          #显示图像
cv2.waitKey(0)