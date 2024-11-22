import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread(r'D:\cv\week11\handball.jpg')
cv2.imshow('original', img1)
temp = cv2.imread(r'D:\cv\week11\ball.jpg')
cv2.imshow('template', temp)
img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY, dstCn=1)  # 转换为单通道灰度图像
tempgray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY, dstCn=1)  # 转换为单通道灰度图像
h, w = tempgray.shape  # 获得模板图像的高度和宽度
res = cv2.matchTemplate(img1gray, tempgray, cv2.TM_SQDIFF)  # 执行匹配
plt.imshow(res, cmap='gray')  # 以灰度图像格式显示匹配结果
plt.title('Matching Result')
plt.axis('off')
plt.show()  # 显示图像
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 返回匹配位置
top_left = min_loc  # 最小值为最佳匹配，获得其位置
bottom_right = (top_left[0] + w, top_left[1] + h)  # 获得匹配范围的右下角位置
cv2.rectangle(img1, top_left, bottom_right, (255, 0, 0), 2)  # 绘制匹配范围,蓝色边框
cv2.imshow('Detected Range', img1)
cv2.waitKey(0)
 