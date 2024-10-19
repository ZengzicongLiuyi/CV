#test2-1.py：读取图像
import cv2
img=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_4)  	#读取图像
print(type(img))            	#输出数据类型
print(img)                  	#输出图像数组
print(img.shape)			#输出数组形状
print(img.dtype)			#输出数组元素的数据类型
print(img.size)				#输出数组元素的个数
