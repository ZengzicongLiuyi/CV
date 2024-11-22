#test7-2.py：多目标匹配
import cv2
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('bee2.jpg')                               #打开输入图像,默认BGR格式
temp=cv2.imread('template.jpg')                         #打开模板图像
img1gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY,dstCn=1)  #转换为单通道灰度图像
tempgray=cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY,dstCn=1)  #转换为单通道灰度图像
th,tw=tempgray.shape                                     #获得模板图像的高度和宽度
img1h,img1w=img1gray.shape
res = cv2.matchTemplate(img1gray,tempgray,cv2.TM_SQDIFF_NORMED)#执行匹配操作
mloc=[]                                                         #用于保存符合条件的匹配位置
threshold = 0.24                                                #设置匹配度阈值
for i in range(img1h-th):
    for j in range(img1w-tw):
        if res[i][j]<=threshold:                                #保存小于阈值的匹配位置
            mloc.append((j,i))
for pt in mloc:
    cv2.rectangle(img1,pt,(pt[0]+tw,pt[1]+th),(255,0,0),2)  #标准匹配位置，蓝色矩形
cv2.imshow('result',img1)                                   #显示结果
cv2.waitKey(0)