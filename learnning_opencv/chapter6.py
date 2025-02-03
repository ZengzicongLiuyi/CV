import cv2
from matplotlib import pyplot as plt

img = cv2.imread('hehua.jpg',0) #0表示灰度图
hist = cv2.calcHist([img],[0],None,[256],[0,256])
hist.shape#(256, 1)
plt.hist(img.ravel(),256);
plt.show()
color=('b','g','r') 
for i,col in enumerate(color):
    #histr = cv2.calcHist([img],[i],None,[256],[0,256])
    histr = cv2.calcHist([img],[i],None,[256],[0,256]) 
    plt.plot(histr,color=col)
    plt.xlim([0,256])#x轴的范围
