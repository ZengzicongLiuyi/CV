# 图像变换
import cv2
 
# 打开图像
image = cv2.imread('five.jpg')
 
# 缩放图像
scaled_image = cv2.resize(image, (500, 500))
 
# 旋转图像
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
 
# 裁剪图像
cropped_image = image[100:300, 100:300]
 
# 显示变换后的图像
cv2.imshow('img',image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()