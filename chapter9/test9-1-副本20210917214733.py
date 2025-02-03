#test9-1.py：使用Haar级联检测器检测人脸
#将用于眼睛和人脸检测的Harr级联检测器文件复制到程序文件位置
import cv2
img=cv2.imread('heard.jpg')                         	#打开输入图像
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)         #转换为灰度图像
#加载人脸检测器
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#加载眼睛检测器
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
faces = face.detectMultiScale(gray)#执行人脸检测
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#绘制矩形标注人脸
    roi_eye = gray[y:y+h, x:x+w]            #根据人脸获得眼睛的检测范围
    eyes = eye.detectMultiScale(roi_eye)    #在人脸范围内检测眼睛
    for (ex,ey,ew,eh) in eyes: #标注眼睛
        cv2.circle(img[y:y+h, x:x+w],(int(ex+ew/2),
                 int(ey+eh/2)),int(max(ew,eh)/2),(0,255,0),2)
cv2.imshow('faces',img)                                   #显示检测结果
cv2.waitKey(0)
