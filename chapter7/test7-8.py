#test7-8.py：应用图像金字塔实现图像融合
import cv2
img1 = cv2.imread(r'D:\cv\chapter7\jiang1.jpg')
img2 = cv2.imread(r'D:\cv\chapter7\jiang2.jpg')
#生成图像1的高斯金字塔，向下采样6次
img = img1.copy()
img1Gaus = [img]
for i in range(6):
    img = cv2.pyrDown(img)
    img1Gaus.append(img)
#生成图像2的高斯金字塔，向下采样6次
img = img2.copy()
img2Gaus = [img]
for i in range(6):
    img = cv2.pyrDown(img)
    img2Gaus.append(img)
#生成图像1的拉普拉斯金字塔，6层
img1Laps = [img1Gaus[5]]
for i in range(5,0,-1):
    img = cv2.pyrUp(img1Gaus[i])
    lap = cv2.subtract(img1Gaus[i-1],img)    #两个图像大小不同时，做减法会出错
    img1Laps.append(lap)
#生成图像2的拉普拉斯金字塔，6层
img2Laps = [img2Gaus[5]]
for i in range(5,0,-1):
    img = cv2.pyrUp(img2Gaus[i])
    lap = cv2.subtract(img2Gaus[i-1],img)
    img2Laps.append(lap)
#拉普拉斯金字塔拼接：图像1每层左半部分与和图像2每层右半部分拼接
imgLaps = []
for la,lb in zip(img1Laps,img2Laps):
    rows,cols,dpt = la.shape
    ls=la.copy()
    ls[:,int(cols/2):]=lb[:,int(cols/2):]
    imgLaps.append(ls)
#从拉普拉斯金字塔恢复图像
img = imgLaps[0]
for i in range(1,6):
    img = cv2.pyrUp(img)
    img = cv2.add(img, imgLaps[i])
#图像1原图像的半部分与和图像2原图像的右左半部分直接拼接
direct = img1.copy()
direct[:,int(cols/2):]=img2[:,int(cols/2):]
cv2.imshow('Direct',direct)             #显示直接拼接结果
cv2.imshow('Pyramid',img)               #显示图像金字塔拼接结果
cv2.waitKey(0)