#test3-6.py：绘制椭圆
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8)+255 #创建一幅白色图像
cv2.ellipse(img,(160,100),(120,50),0,0,360,(255,0,0),5)#画椭圆，蓝色边框
cv2.ellipse(img,(160,100),(60,15),0,0,360,(0,255,0),51)#画椭圆，绿色填充
cv2.imshow('draw',img)          #显示图像
cv2.waitKey(0),vg