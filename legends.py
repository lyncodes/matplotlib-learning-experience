import numpy as np
import matplotlib.pyplot as plt

# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]#c的索引步长为-1，即从尾开始索引，即倒序

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')#--线形,------------并且添加上了label
ax.plot(a, d, 'g:', label='Data length')#：线形
ax.plot(a, c + d, 'r', label='Total message length')#不带符号，为实线

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')#hex color
#get_frame()函数返回一个rectangle，用于放置三个label，即是中间哪个绿色的方块
plt.savefig("legends.jpg")
plt.show()