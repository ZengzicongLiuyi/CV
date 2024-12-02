#test8-2.py锛氫紭鍖栧搱閲屾柉瑙�
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('cube.jpg')                #鎵撳紑鍥惧儚锛岄粯璁GR鏍煎紡
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #杞崲涓虹伆搴﹀浘鍍�
gray = np.float32(gray)                     #杞崲涓烘诞鐐圭被鍨�
dst = cv2.cornerHarris(gray,8,7,0.10)       #鏌ユ壘鍝堥噷鏂
r, dst = cv2.threshold(dst,0.01*dst.max(),255,cv2.THRESH_BINARY)#浜屽€煎寲闃堝€煎鐞�
dst = np.uint8(dst)                         #杞崲涓烘暣鍨�
r,l,s,cxys = cv2.connectedComponentsWithStats(dst)#鏌ユ壘璐ㄧ偣鍧愭爣
cif = (cv2.TERM_CRITERIA_EPS + 
              cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)#瀹氫箟浼樺寲鏌ユ壘鏉′欢
corners = cv2.cornerSubPix(gray,
             np.float32(cxys),(5,5),(-1,-1),cif)#鎵ц浼樺寲鏌ユ壘
res = np.hstack((cxys,corners))                 #鍫嗗彔鏋勯€犳柊鏁扮粍锛屼究浜庢爣娉ㄨ
res = np.int0(res)                              #杞崲涓烘暣鍨�
img[res[:,1],res[:,0]]=[0,0,255]                #灏嗗搱閲屾柉瑙掑搴斿儚绱犺缃负绾㈣壊
img[res[:,3],res[:,2]] = [0,255,0]              #灏嗕紭鍖栫粨鏋滃儚绱犺缃负缁胯壊
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)       #杞崲涓篟GB鏍煎紡
plt.imshow(img)
plt.axis('off')
plt.show()                                      #鏄剧ず妫€娴嬬粨鏋�