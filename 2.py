import cv2
import numpy as np

# 选择图像文件
image = cv2.imread('C:/Users/Administrator/Desktop/222.png')  # 替换为你的图像路径

# 如果图像加载失败，返回错误信息
if image is None:
    print("Error: Unable to load image")
else:
    # 定义一个矩形框，用户可以根据实际情况调整位置和大小
    # 这个矩形框告诉 `grabCut` 初始的前景区域
    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # (x, y, width, height)

    # 创建一个 mask，这个 mask 在开始时全部为 0
    mask = np.zeros(image.shape[:2], np.uint8)

    # 定义两个背景和前景模型，这两个模型会被 `grabCut` 算法使用
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # 使用 grabCut 算法进行图像分割
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # `grabCut` 之后，mask 的值会更新为不同的标签：
    # 0: 背景, 1: 确定的前景, 2: 可能的背景, 3: 可能的前景
    # 我们需要将 mask 转换为二值图像，表示前景和背景
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # 使用 mask 来提取前景
    result = image * mask2[:, :, np.newaxis]

    # 显示结果
    cv2.imshow('Original Image', image)
    cv2.imshow('Foreground Extraction', result)

    # 等待按键并关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
