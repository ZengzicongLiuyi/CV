#test9-3.py：检测摄像头视频中的人脸
import cv2
capture = cv2.VideoCapture(0)   #创建视频捕捉器对象
if not capture.isOpened:
    print('不能打开摄像头')
    exit(0)                     #不能打开摄像头时结束程序
#加载人脸检测器
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#加载眼睛检测器
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
while True:
    ret, frame = capture.read()                             #读摄像头的帧
    if frame is None:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)           #转换为灰度图像    
    faces = face.detectMultiScale(gray)                     #执行人脸检测
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)    #绘制矩形标注人脸      
        roi_eye = gray[y:y+h, x:x+w]                        #根据人脸获得眼睛的检测范围
        eyes = eye.detectMultiScale(roi_eye)                #在人脸范围内检测眼睛
        for (ex,ey,ew,eh) in eyes:                          #标注眼睛
            cv2.circle(frame[y:y+h, x:x+w],(int(ex+ew/2),
                 int(ey+eh/2)),int(max(ew,eh)/2),(0,255,0),2)  
    cv2.imshow('faces',frame)                               #显示帧
    key = cv2.waitKey(30)
    if key == 27:                                           #按Esc键结束程序
        break
