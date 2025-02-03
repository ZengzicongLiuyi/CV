#test9-5.py：EigenFaces人脸识别
import cv2
import numpy as np
img11=cv2.imread('xl11.jpg',0)                         	#打开图像，灰度图
img12=cv2.imread('xl12.jpg',0)                         	#打开图像，灰度图
img13=cv2.imread('xl13.jpg',0)                         	#打开图像，灰度图
img21=cv2.imread('xl21.jpg',0)                         	#打开图像，灰度图
img22=cv2.imread('xl22.jpg',0)                         	#打开图像，灰度图
img23=cv2.imread('xl23.jpg',0)                         	#打开图像，灰度图
train_images=[img11,img12,img13,img21,img22,img23]      #创建训练图像数组
labels=np.array([0,0,0,1,1,1])          #创建标签数组，0和1表示对应的训练图像数组中人脸的身份
recognizer=cv2.face.EigenFaceRecognizer_create()#创建FisherFaces识别器
recognizer.train(train_images,labels)                   #执行训练操作
testimg=cv2.imread('test1.jpg',0)                       #打开测试图像
label,confidence=recognizer.predict(testimg)            #识别人脸
print('匹配标签：',label)
print('可信度：',confidence)

