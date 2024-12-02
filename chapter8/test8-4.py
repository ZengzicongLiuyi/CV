#test8-4.py：FAST关键点检测
import cv2
img = cv2.imread('cube.jpg')                    #打开图像，默认BGR格式
fast = cv2.FastFeatureDetector_create()         #创建FAST检测器
kp = fast.detect(img,None)                      #检测关键点，不使用掩模
img2 = cv2.drawKeypoints(img, kp, None, color=(0,0,255))#绘制关键点
cv2.imshow('FAST points',img2)          #显示绘制了关键点的图像
fast.setThreshold(20)                   #设置阈值，默认阈值为10
kp = fast.detect(img,None)              #检测关键点，不使用掩模
n=0
for p in kp:
    print("第%s个关键点，坐标："%(n+1),p.pt,'响应强度：',p.response,
            '邻域大小：',p.size,'角度：',p.angle)
    n+=1
img3 = cv2.drawKeypoints(img, kp, None, color=(0,0,255))
cv2.imshow('Threshold20',img3)          #显示绘制了关键点的图像
cv2.waitKey(0)