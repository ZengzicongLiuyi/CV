# 图像增强
import cv2
 
# 打开图像
image = cv2.imread('five.jpg')
 
# 增强对比度
enhanced_image = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
 
# 显示增强后的图像

cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()