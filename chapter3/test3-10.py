#test3-10.py：响应鼠标事件
import numpy as np
import cv2
img=np.zeros((200,320,3), np.uint8)+255 #创建一幅白色图像

def draw(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
       cv2.circle(img,(x,y),20,(255,0,0),-1)#双击鼠标左键时画圆
    elif event==cv2.EVENT_RBUTTONDBLCLK:
       cv2.rectangle(img,(x,y),(x+20,y+20),(0,0,255),-1)#双击鼠标右键时画矩形

cv2.namedWindow('drawing')
cv2.setMouseCallback('drawing',draw)
while(True):
    cv2.imshow('drawing',img)          #显示图像
    k = cv2.waitKey(1)
    if k == 27:                         #按【Esc】键时结束循环
        break
cv2.destroyAllWindows()
