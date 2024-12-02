#test8-5.py：SIFT关键点检测
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('five.jpg')                    #打开图像，默认BGR格式
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)      #转换为灰度图像
sift = cv2.SIFT_create()            #创建SIFT对象
kp = sift.detect(gray,None)                     #检测关键点
img2 = cv2.drawKeypoints(img,kp,None,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) #绘制关键点
img2= cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)      #转换为RGB图像
plt.imshow(img2)
plt.axis('off')
plt.show()                                      #显示绘制了关键点的图像