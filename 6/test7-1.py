import cv2
image = cv2.imread(r'D:\cv\6\mango.jpg')
height, width = image.shape[:2]
new_width = int(width * 0.5)
new_height = int(height * 0.5)
resized_image = cv2.resize(image, (new_width, new_height))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# 进行 Canny 边缘检测
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()