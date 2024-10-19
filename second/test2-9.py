#test2-9.py：操作彩色图像
#创建一幅彩色图像，图像的上、中、下三个部分依次为蓝色、绿色和红色，
#程序每隔1秒钟轮换三个部分的颜色。
import cv2
import numpy
img=numpy.zeros((240,320,3),dtype=numpy.uint8)  #创建图像
r0=0
r1=1
r2=2
while True:
    img[:80,:,r0]=255                       #通道r0上三分之一颜色值设为255
    img[80:160,:,r1]=255                    #通道r1中部三分之一颜色值设为255
    img[160:,:,r2]=255                      #通道r2下三分之一颜色值设为255
    cv2.imshow('ColorImg',img)
    key=cv2.waitKey(1000)                   #延迟1秒
    img[:,:,:]=0                            #像素全部置0
    t=r0                                    #轮换通道序号
    r0=r1
    r1=r2
    r2=t
    if key==27:
        break                               #按【Esc】键结束       
    
