#test2-2.py：将图像存入文件
import cv2
import numpy
img=numpy.zeros((50,50),dtype=numpy.uint8)+255
# 创建 50*50 的黑色正方形图像
# +255 白色
cv2.imwrite('mypic2-1.jpg',img)  # 保存图像
