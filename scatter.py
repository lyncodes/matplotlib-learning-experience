import numpy as np
import matplotlib.pyplot as plt



N = 500
x = np.random.rand(N)#在0-1之间生成随机数
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * y)**2  # 0 to 15 point radii
#s:   size of points
plt.scatter(x, y, s=area, c=colors, alpha=0.5)#以x坐标的函数为点的大小，x越大，直径越大
plt.savefig("scatter.jpg")
plt.show()