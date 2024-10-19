#test3-3.py：绘制直线
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8) #创建一幅黑色图像
cv2.line(img,(0,0),(320,200),(0,0,255),10)#画对角线1，红色
cv2.line(img,(320,0),(0,200),(0,255,0),5)#画对角线2，绿色
cv2.imshow('draw',img)          #显示图像
cv2.waitKey(0)