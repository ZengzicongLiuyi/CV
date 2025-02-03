import cv2
import numpy as np
import tensorflow


# 模型文件和配置文件路径
model_path = r'C:\Users\Administrator\Desktop\1111\opencv_face_detector_uint8.pb'
config_path = r'C:\Users\Administrator\Desktop\1111\opencv_face_detector.pbtxt'

# 加载 OpenCV 的深度学习模块 (DNN)
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

# 读取图像
image = cv2.imread(r'C:\Users\Administrator\Desktop\123.png')

# 获取图像的高和宽
height, width, _ = image.shape

# 将图像转换为 blob（适合神经网络处理的格式）
blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104, 177, 123), swapRB=True, crop=False)

# 将 blob 输入到网络中
net.setInput(blob)

# 获取模型输出
detections = net.forward()

# 遍历所有检测到的人脸
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    # 如果置信度大于阈值，认为检测到人脸
    if confidence > 0.5:
        # 获取边界框的坐标
        box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
        (startX, startY, endX, endY) = box.astype("int")

        # 在图像上绘制边界框
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# 显示检测结果
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
