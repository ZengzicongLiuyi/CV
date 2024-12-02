#test8-1.py锛氬搱閲屾柉瑙掓娴嬪櫒
import cv2
import numpy as np
img=cv2.imread('cube.jpg')                         	#鎵撳紑杈撳叆鍥惧儚
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)             #杞崲涓虹伆搴﹀浘鍍�
gray = np.float32(gray)                                 #杞崲涓烘诞鐐圭被鍨�
dst = cv2.cornerHarris(gray,10,5,0.001)                   #鎵ц瑙掓娴�
img[dst>0.02*dst.max()]=[0,0,255]                       #灏嗚璁剧疆涓虹孩鑹�
cv2.imshow('dst',img)                                   #鏄剧ず妫€娴嬬粨鏋�
cv2.waitKey(0)
