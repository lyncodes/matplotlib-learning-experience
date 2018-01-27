import numpy as np
import matplotlib.pyplot as plt
#准备数学上的离散数据点
x1 = np.linspace(0,5)
x2 = np.linspace(0,2)

y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(2*np.pi*x2)

plt.subplot(2, 1, 1)
#####分成2x1的结构。2 rows，1 column，占用第一个位置
plt.plot(x1, y1, 'o-')
#以o-进行线的特性规划，o，表示圆圈，-表示以实线穿起来
plt.title('2 subplots')
plt.ylabel('damped oscillation')

plt.subplot(2, 1, 2)
#####分成2x1的结构。2 rows，1 column，占用第一个位置
plt.plot(x2, y2, '.-')
#以o-进行线的特性规划，.表示圆圈，-表示以实线穿起来
plt.xlabel('time (s)')
plt.ylabel('Undamped')


plt.savefig("subplots.jpg")
plt.show()