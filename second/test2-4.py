#test2-4.py：等待按键
import cv2
img=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_COLOR_2)  	#读取图像，缩小为原来的1/2
cv2.imshow('lena',img)          #显示图像
key=0
while key!=27:                  #按Esc键时终止循环
    key=cv2.waitKey()           #等待按键
    
cv2.destroyWindow('lena')       #关闭图像窗口
