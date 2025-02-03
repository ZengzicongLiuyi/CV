# 分割Olivetti Faces
# 纽约大学提供的人脸图片数据集，包含40个人（每人10张人脸图像）的400张人脸图像。下载地址为https://cs.nyu.edu/~roweis/data/olivettifaces.gif。
# 将olivettifaces.jpg尺寸调整为940*1140
# 分割为20行、20列个人脸图像
#
import cv2
import numpy as np
img = cv2.imread('olivettifaces.jpg')
faces=[np.hsplit(row,20) for row in np.vsplit(img,20)]#分解图像，20行20列
r=1
c=0
for a in faces:    
    for b in a:        
        c+=1
        cv2.imwrite('face%02d%02d.jpg'%(r,c),b) #将每个人脸图像存入文件
        if c==10:
            c=0
            r+=1