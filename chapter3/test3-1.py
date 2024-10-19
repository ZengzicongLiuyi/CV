#test3-1.py：创建窗口
import numpy
import cv2
img=numpy.zeros((240,320),dtype=numpy.uint8)    #创建黑色图像
img[70:170,110:210]=255                         #设置白色区域
cv2.namedWindow('test3-1',cv2.WINDOW_NORMAL)    #创建普通窗口
cv2.imshow('test3-1',img)                       #在窗口中显示图像
cv2.waitKey(5000)

cv2.destroyAllWindows()

# cv2.destoryWindows('test3-1')