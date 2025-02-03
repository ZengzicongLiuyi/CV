#test7-10.py：交互式前景提取2
import cv2
import numpy as np
img = cv2.imread(r'D:\cv\chapter7\cup.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bg = np.zeros((1,65),np.float64)
fg = np.zeros((1,65),np.float64)
rect = (50,50,400,300)              
cv2.grabCut(img,mask,rect,bg,fg,5,cv2.GC_INIT_WITH_RECT)
imgmask = cv2.imread(r'D:\cv\chapter7\cup2.jpg')  
cv2.imshow('mask image',imgmask)
mask2 = cv2.cvtColor(imgmask,cv2.COLOR_BGR2GRAY,dstCn=1)
mask[mask2==0]=0
mask[mask2==255]=1
cv2.grabCut(img,mask,None,bg,fg,5,cv2.GC_INIT_WITH_MASK)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
cv2.imshow('grabCut',img)
cv2.waitKey(0)