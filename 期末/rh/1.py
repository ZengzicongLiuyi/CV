import cv2
import numpy as np

def stitch_images(image1_path, image2_path, output_path="stitched_image.jpg"):
    # 读取两张图像
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # 转换为灰度图像
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 使用 ORB 特征检测器
    orb = cv2.ORB_create()

    # 检测关键点和描述符
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # 使用 BFMatcher 进行特征点匹配
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)  # 按距离排序，距离越小越匹配

    # 提取匹配点
    points1 = np.array([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 2)
    points2 = np.array([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 2)

    # 计算单应性矩阵
    H, mask = cv2.findHomography(points2, points1, cv2.RANSAC)

    # 将图像2变换到图像1的平面
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]
    panorama = cv2.warpPerspective(image2, H, (width1 + width2, height1))
    panorama[0:height1, 0:width1] = image1

    # 裁剪掉黑色边缘
    gray_panorama = cv2.cvtColor(panorama, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_panorama, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv2.boundingRect(contours[0])
    cropped_panorama = panorama[y:y+h, x:x+w]

    # 保存并显示结果
    cv2.imwrite(output_path, cropped_panorama)
    cv2.imshow("Stitched Image", cropped_panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 示例使用
image1_path = "R-C.jpg"  # 替换为你的第一张图像路径
image2_path = "OIP-C (1).jpg"  # 替换为你的第二张图像路径
stitch_images(image1_path, image2_path)
