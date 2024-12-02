import cv2
 
# 打开图像
image = cv2.imread('hehua.jpg')
 
# 应用边缘检测
edges = cv2.Canny(image, 100, 200)
 
# 显示边缘检测后的图像
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()