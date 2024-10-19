#test2-5.py：播放视频
import cv2
vc=cv2.VideoCapture('c919.mp4')  	#创建VideoCapture对象
fps=vc.get(cv2.CAP_PROP_FPS)            #读取视频帧率
size=(vc.get(cv2.CAP_PROP_FRAME_WIDTH),
      vc.get(cv2.CAP_PROP_FRAME_HEIGHT)) #读取视频大小
print('帧率：',fps)
print('大小：',size)
success,frame=vc.read()                 #读第1帧
while success:                          #循环读视频帧，直到视频结束    
    cv2.imshow('C919',frame)         #在窗口中显示帧图像
    success,frame=vc.read()             #读下一帧
    key=cv2.waitKey(25)
    if key==27:                         #按Esc键退出
        break
vc.release()                            #关闭视频
