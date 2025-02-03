#test9-2.py：使用Harr级联检测器检测猫脸
import cv2
img=cv2.imread('cat2.jpg')                         	#打开输入图像
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)         #转换为灰度图像
#加载猫脸检测器
face = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
faces = face.detectMultiScale(gray)#执行猫脸检测
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#绘制矩形标注猫脸
cv2.imshow('faces',img)                           #显示检测结果
cv2.waitKey(0)
