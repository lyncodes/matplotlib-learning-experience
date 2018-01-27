import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

fig, ax = plt.subplots()

ax.fill(x, y, zorder=5.1)

####这个zorder啊，是表示一个状态，fill的zorder比较大，所以后渲染

#####fill()函数，画出filled polygons


ax.grid(True, zorder=5)#grid的zorder表较小，所以先渲染
#这样，我们看到的图就是填充好的色块在网格的上方
plt.title("color block is above the grid")



x = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x)
y2 = np.sin(3 * x)

fig, ax = plt.subplots()
ax.fill(x, y1, 'b', x, y2, 'r', alpha=0.5, zorder=1)
ax.grid(True, zorder=2)
plt.title("color block is under the grid")


plt.savefig("filled plot.jpg")
plt.show()