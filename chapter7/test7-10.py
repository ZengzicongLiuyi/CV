#test7-10.py：交互式前景提取2
import cv2
import numpy as np
img = cv2.imread('hehua.jpg')
mask = np.zeros(img.shape[:2],np.uint8)#定义原始掩模
bg = np.zeros((1,65),np.float64)
fg = np.zeros((1,65),np.float64)
rect = (50,50,400,300)              #根据原图设置包含前景的矩形大小
cv2.grabCut(img,mask,rect,bg,fg,5,cv2.GC_INIT_WITH_RECT)#第1次提取前景,矩形模式
imgmask = cv2.imread('hehua2.jpg')  #读取已标注的掩模图像
cv2.imshow('mask image',imgmask)
mask2 = cv2.cvtColor(imgmask,cv2.COLOR_BGR2GRAY,dstCn=1)#转换未单通道灰度图像
mask[mask2==0]=0#根据掩模图像，将掩模图像中白黑色像素对应的原始掩模像素设置为0
mask[mask2==255]=1#根据掩模图像，将掩模图像中白色像素对应的原始掩模像素设置为1
cv2.grabCut(img,mask,None,bg,fg,5,cv2.GC_INIT_WITH_MASK)#第2次提取前景，掩模模式
#将返回的掩模中像数值为0或2像素设置为0（确认为背景），
#所有1或3的像素设置为1（确认为前景）
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]#将掩模与原图像相乘获得分割出来的前景图像
cv2.imshow('grabCut',img)#显示获得的前景
cv2.waitKey(0)