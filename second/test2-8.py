#test2-8.py：操作灰度图像
import cv2
import numpy
img=numpy.zeros((240,320),dtype=numpy.uint8)  	#创建图像
n=0
while True:
    cv2.imshow('GrayImg',img)
    n+=20
    img[:,:]=n                                  #更改图像灰度
    print(img[1,1])                             #输出一个像素值
    key=cv2.waitKey(1000)                       #延迟1秒
    if key==27:
        break                                   #按【Esc】键结束       
    
