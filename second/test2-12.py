#test2-12.py：合并图像通道
import cv2
img=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_COLOR_2)#读图像，缩小为原来的1/2
cv2.imshow('lena',img)          	#显示原图像
b,g,r=cv2.split(img)            	#按通道拆分图像
rgb=cv2.merge([r,g,b])          	#按新顺序合并
gbr=cv2.merge([g,b,r])          	#按新顺序合并
cv2.imshow('lena_RGB',rgb)        	#显示合并图像
cv2.imshow('lena_GBR',gbr)        	#显示合并图像
cv2.waitKey(0)