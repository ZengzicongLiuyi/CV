# test7-9.py：交互式前景提取1
import cv2
import numpy as np
img = cv2.imread(r'D:\cv\chapter7\hehua.jpg')
cv2.imshow('original', img)
mask = np.zeros(img.shape[:2], np.uint8)  # 定义与原图大小相同的掩模
bg = np.zeros((1, 65), np.float64)
fg = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 300)  # 根据原图设置包含前景的矩形大小
cv2.grabCut(img, mask, rect, bg, fg, 5, cv2.GC_INIT_WITH_RECT)  # 提取前景
# 将返回的掩模中像数值为0或2像素设置为0（确认为背景），
# 所有1或3的像素设置为1（确认为前景）
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]  # 将掩模与原图像相乘获得分割出来的前景图像
cv2.imshow('grabCut', img)  # 显示获得的前景
cv2.waitKey(0)
