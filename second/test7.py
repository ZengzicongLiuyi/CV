import cv2
img1 = cv2.imread('lena.jpg', cv2.IMREAD_REDUCED_COLOR_2)  
cv2.imshow('Original Image', img1)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
