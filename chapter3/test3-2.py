#test3-2.py：调整窗口大小
import cv2
img=cv2.imread('lena.jpg')  	#读取图像
s=img.shape
print("s:",s)
cv2.imshow('lena',img)          #显示图像
key=cv2.waitKey()
cv2.resizeWindow('lena',(s[0]//2,s[1]//2))
cv2.waitKey(0)