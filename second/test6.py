import cv2

img = cv2.imread('lena.jpg')

if img is None:
    print("Error: Image not found. Please check the file path.")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray_img)

    resized_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    cv2.imshow('Resized Image', resized_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
