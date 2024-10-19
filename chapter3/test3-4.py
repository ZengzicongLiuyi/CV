#test3-4.py：绘制矩形
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8) #创建一幅黑色图像
cv2.rectangle(img,(20,20),(300,180),(255,0,0),10)#画矩形，蓝色边框
cv2.rectangle(img,(70,70),(250,130),(0,255,0),2)#画矩形，绿色填充
cv2.imshow('draw',img)          #显示图像
cv2.waitKey(0)