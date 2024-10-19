import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# 加载图像
img_path = '4\bee.jpg'  # 替换为你的图像路径
original_image = Image.open(img_path)

# 设置参数
frames = 60          # 动画帧数
scale_min = 0.1      # 最小缩放比例（10%）
scale_steps = 20     # 缩放步数
scale_max = 1.0      # 最大缩放比例（100%）

def update(frame):
    # 计算当前缩放比例
    if frame < frames // 2:
        scale = scale_min + (scale_max - scale_min) * (frame / (frames // 2))
    else:
        scale = scale_max - (scale_max - scale_min) * ((frame - frames // 2) / (frames // 2))

    # 计算当前旋转角度
    angle = frame * (360 / frames)  # 每帧旋转的角度

    # 进行图像缩放和旋转
    resized_image = original_image.resize((int(original_image.width * scale), 
                                            int(original_image.height * scale)))
    rotated_image = resized_image.rotate(angle, expand=True)

    # 更新图像数据
    ax.clear()
    ax.imshow(rotated_image)
    ax.axis('off')  # 不显示坐标轴

# 创建动画
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=frames, interval=50)

plt.show()
