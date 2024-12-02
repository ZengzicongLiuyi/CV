#读取图片/视频/摄像头
import cv2
img = cv2.imread('five.jpg')

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('output.jpg',img)



























