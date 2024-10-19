#test3-8.py：绘制文字
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8)+255 #创建一幅白色图像
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img,'Python',(50,60), font,2,(255,0,0),2,cv2.LINE_AA)#绘制文字
# putText()不可绘制中文
cv2.putText(img,'Python',(50,100), font,2,(255,0,0),2,cv2.LINE_AA,True)#绘制镜像文字
cv2.imshow('draw',img)          #显示图像
cv2.waitKey(0)
'''字体类型
cv2.FONT_HERSHEY_SIMPLEX
cv2.FONT_HERSHEY_PLAIN
cv2.FONT_HERSHEY_DUPLEX
cv2.FONT_HERSHEY_COMPLEX
cv2.FONT_HERSHEY_TRIPLEX
cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.FONT_ITALIC
'''
