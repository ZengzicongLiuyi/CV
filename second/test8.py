import cv2
import numpy as np
img = np.zeros((240, 320, 3), dtype=np.uint8)
square_size = 100
top_left = ((320 - square_size) // 2, (240 - square_size) // 2)
bottom_right = (top_left[0] + square_size, top_left[1] + square_size)
img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = (0, 0, 255)
cv2.imwrite('test8.jpg', img)
