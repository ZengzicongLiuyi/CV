#test5-8.py：轮廓长度
import cv2
import numpy as np
img=cv2.imread('shape2.jpg')                            #读取图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)               #转化为灰度图像
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)  #二值化阈值处理
c,h=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
for n in range(len(c)):
    m=cv2.arcLength(c[n],True)                  #计算轮廓长度
    print('轮廓%s的长度：'%n,m)                  #输出轮廓长度