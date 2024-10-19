import cv2
img1 = cv2.imread('lena.jpg', cv2.IMREAD_REDUCED_COLOR_2)
rect_width = 80
rect_height = 100
top_left = (50, 50)
img1[top_left[1]:top_left[1] + rect_height, top_left[0]:top_left[0] + rect_width] = (0, 0, 0)
cv2.imshow('Image with Black Rectangle', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('lena_with_black_rectangle.jpg', img1)
