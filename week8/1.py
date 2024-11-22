import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'1.png')
# 1. 图像缩放
def resize_image(image, scale_factor):
    width = int(image.shape[1] * scale_factor)
    height = int(image.shape[0] * scale_factor)
    resized_image = cv2.resize(image, (width, height))
    return resized_image
# 2. 图像旋转
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image
# 3. 图像平移
def translate_image(image, tx, ty):
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image
# 4. 图像透视变换
def perspective_transform(image):
    # 定义透视变换前后的4个点
    rows, cols = image.shape[:2]
    pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])
    pts2 = np.float32([[10, 100], [cols - 100, 50], [100, rows - 10], [cols - 50, rows - 50]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))
    return perspective_image
scaled_image = resize_image(image, 0.5)  
rotated_image = rotate_image(image, 45)
translated_image = translate_image(image, 100, 50)
perspective_image = perspective_transform(image)
# 1. 显示缩放后的图像
cv2.imshow('缩放', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 2. 显示旋转后的图像
cv2.imshow('旋转', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 3. 显示平移后的图像
cv2.imshow('平移', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 4. 显示透视变换后的图像
cv2.imshow('透视', perspective_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
