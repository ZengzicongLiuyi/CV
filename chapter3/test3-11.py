#test3-11.py：使用跟踪栏
import numpy as np
import cv2
img=np.zeros((120,400,3), np.uint8) #创建一幅黑色图像
def doChange(x):
    b=cv2.getTrackbarPos('B','trakbar')
    g=cv2.getTrackbarPos('G','trakbar')
    r=cv2.getTrackbarPos('R','trakbar')
    img[:]=[b,g,r]                          #更改图像
cv2.namedWindow('trakbar')
cv2.createTrackbar('B','trakbar',0,255,doChange)#创建跟踪栏
cv2.createTrackbar('G','trakbar',0,255,doChange)
cv2.createTrackbar('R','trakbar',0,255,doChange)
while(True):
    cv2.imshow('trakbar',img)           #显示图像
    k = cv2.waitKey(1)
    if k == 27:                         #按【Esc】键时结束循环
        break
cv2.destroyAllWindows()
