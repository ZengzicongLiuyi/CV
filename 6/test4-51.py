# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# # 读取图像
# image = cv2.imread(r'D:\cv\6\mango.jpg', 0)

# # 定义结构元素
# kernel = np.ones((5,5), np.uint8)

# # 腐蚀操作
# erosion = cv2.erode(image, kernel, iterations=1)

# # 膨胀操作
# dilation = cv2.dilate(image, kernel, iterations=1)

# # 开操作（先腐蚀后膨胀）
# opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# # 闭操作（先膨胀后腐蚀）
# closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# # 显示原始图像和处理后的图像
# images = [image, erosion, dilation, opening, closing]
# titles = ['Original Image', 'Erosion', 'Dilation', 'Opening', 'Closing']

# for i in range(5):
#     plt.subplot(2, 3, i+1)
#     plt.imshow(images[i], cmap='gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# plt.tight_layout()
# plt.show()



import cv2
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('bee2.bmp')

# 均值滤波
mean_filtered = cv2.blur(image, (5, 5))

# 高斯滤波
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)

# 方框滤波
box_filtered = cv2.boxFilter(image, -1, (5, 5))

# 中值滤波
median_filtered = cv2.medianBlur(image, 5)

# 双边滤波
bilateral_filtered = cv2.bilateralFilter(image, 9, 75, 75)

# 显示原始图像和滤波后的图像
images = [image, mean_filtered, gaussian_filtered, box_filtered, median_filtered, bilateral_filtered]
titles = ['Original Image', 'Mean Filter', 'Gaussian Filter', 'Box Filter', 'Median Filter', 'Bilateral Filter']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
import cv2
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('bee2.bmp')

# 均值滤波
mean_filtered = cv2.blur(image, (5, 5))

# 高斯滤波
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)

# 方框滤波
box_filtered = cv2.boxFilter(image, -1, (5, 5))

# 中值滤波
median_filtered = cv2.medianBlur(image, 5)

# 双边滤波
bilateral_filtered = cv2.bilateralFilter(image, 9, 75, 75)

# 显示原始图像和滤波后的图像
images = [image, mean_filtered, gaussian_filtered, box_filtered, median_filtered, bilateral_filtered]
titles = ['Original Image', 'Mean Filter', 'Gaussian Filter', 'Box Filter', 'Median Filter', 'Bilateral Filter']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()