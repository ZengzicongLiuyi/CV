# import numpy as np
# import matplotlib.pyplot as plt

# def rounded_rectangle(x, y, width, height, radius, num_points=100):
#     """生成圆角矩形的坐标"""
#     radius = min(radius, width / 2, height / 2)
#     theta = np.linspace(0, np.pi / 2, num_points)
#     top_left_x = x + radius * np.cos(theta)
#     top_left_y = y + radius * np.sin(theta)
#     top_right_x = x + width - radius + radius * np.cos(theta)
#     top_right_y = y + radius * np.sin(theta) 
#     bottom_right_x = x + width - radius + radius * np.cos(theta)
#     bottom_right_y = y + height - radius + radius * np.sin(theta)
#     bottom_left_x = x + radius * np.cos(theta) 
#     bottom_left_y = y + height - radius + radius * np.sin(theta)
#     all_x = np.concatenate([top_left_x, top_right_x, bottom_right_x[::-1], bottom_left_x[::-1]])
#     all_y = np.concatenate([top_left_y, top_right_y, bottom_right_y[::-1], bottom_left_y[::-1]])
#     return all_x, all_y
# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# x, y, width, height, radius = 1, 1, 4, 2, 0.5
# all_x, all_y = rounded_rectangle(x, y, width, height, radius)
# ax.fill(all_x, all_y, color='blue', alpha=0.6)  # 填充颜色
# plt.xlim(0, 6)
# plt.ylim(0, 4)
# plt.gca().set_axis_off()  # 不显示坐标轴
# plt.show()




import numpy as np
import matplotlib.pyplot as plt
def heart_shape(t):
    """返回心形的 x, y 坐标"""
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y
t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_shape(t)
fig, ax = plt.subplots()
ax.plot(x, y, color='red')
ax.fill(x, y, color='red', alpha=0.6)
ax.set_aspect('equal')
plt.axis('off') 
plt.title("Love Heart Shape")
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        plt.scatter(event.xdata, event.ydata, color='blue', s=50)
        plt.draw()  
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
