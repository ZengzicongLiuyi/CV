import cv2
import numpy as np

# 读取图像
image = cv2.imread(r'D:\cv\6\mango.jpg', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# 定义核
kernel = np.ones((3, 3), np.uint8)

# 应用开运算（先腐蚀后膨胀）去除噪声点
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# 应用闭运算（先膨胀后腐蚀）去除小线条
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

# 反转图像
denoised_image = cv2.bitwise_not(closing)

# 显示和保存处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Denoised Image', denoised_image)
cv2.imwrite('denoised_image.jpg', denoised_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
