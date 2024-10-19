import cv2
img=cv2.imread('lena.jpg',cv2.IMREAD_REDUCED_COLOR_2)
cv2.imshow('lena',img)         
b=img[:,:,0]                  
g=img[:,:,1]                   
r=img[:,:,2]                    
cv2.imshow('lena_B',b)          
cv2.imshow('lena_G',g)          
cv2.imshow('lena_R',r)         
cv2.waitKey(0)
