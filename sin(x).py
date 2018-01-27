#draw a simple sin(x) function plot

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,2,0.01)#自变量
s = 1 + np.sin(5*np.pi*t)#因变量
#一个"Figure"意味着用户交互的整个窗口。在这个figure中容纳着"subplots"。
#整个图像为一个Figure对象。在Figure对象中可以包含一个或者多个Axes对象
#plt.subplot(221) # 第一行的左图
#plt.subplot(222) # 第一行的右图
#plt.subplot(212) # 第二整行
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', 
	title='The voltage graph.')
ax.grid()
fig.savefig("sin(x).jpg")
plt.show()

