import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image
import matplotlib.pyplot as plt
# 创建一幅白色图像
img = np.zeros((200, 320, 3), np.uint8) + 255 
fontpath = "STSONG.TTF"  # 指定字体文件名    
font1 = ImageFont.truetype(fontpath, 36)  # 载入字体，设置字号
img_pil = Image.fromarray(img)  # 转换为PIL支持格式
draw = ImageDraw.Draw(img_pil)  # 创建Draw对象
draw.text((50, 60), '计算机视觉', font=font1, fill=(0, 0, 0))  # 绘制文字
img = np.array(img_pil)  # 转换为图像数组
# 使用matplotlib显示图像 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')  # 不显示坐标轴
plt.show()
