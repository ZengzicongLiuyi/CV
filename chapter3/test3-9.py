#test3-9.py：绘制箭头
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8)+255 #创建一幅白色图像
cv2.arrowedLine(img,(50,50),(50,150), (0,0,255),2 )#绘制红色垂直箭头
cv2.arrowedLine(img,(50,50),(300,50), (0,0,255),2) #绘制红色水平箭头
cv2.imshow('draw',img)          #显示图像
cv2.waitKey(0)