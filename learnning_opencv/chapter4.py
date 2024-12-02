import cv2
 
# 打开图像
image = cv2.imread('hehua.jpg')
 
# 创建颜色范围
lower_red = (0, 50, 50)
upper_red = (255, 255, 255)
 
# 应用颜色分割
mask = cv2.inRange(image, lower_red, upper_red)
 
# 显示分割后的图像
cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()