#test2-6.py：将视频写入文件
import cv2
vc=cv2.VideoCapture('test2-5.mp4')  			#创建VideoCapture对象
fps=vc.get(cv2.CAP_PROP_FPS)            		#读取视频帧率
size=(int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),
      int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))) 	#读取视频大小
vw=cv2.VideoWriter('test2-6out.avi',			#设置保存视频的文件名
                   cv2.VideoWriter_fourcc('X','V','I','D'),#设置视频解码器格式
                   fps,size)							 #设置帧速率和大小
success,frame=vc.read()                 		#读第1帧
while success:                          			#循环读视频帧，直到视频结束    
    vw.write(frame)                     			#将帧写入文件
    success,frame=vc.read()             		#读下一帧
vc.release()                            			#关闭视频
