import numpy as np

import matplotlib.pyplot as plt

np.random.seed()
######seed()函数，用一套特殊的算法，生成一系列随机数
##不给参数的话，seed（）函数以系统时间为参数生成随机数，这样每次生成的随机数则不同
#如果给定seed（）一个相同的参数，则每次生成的随机数是一样的


#生成数据
mean = 100
sigma = 15
rand = np.random.randn(500)#每次运行的值都不一样####
x = mean + sigma*rand#randn()函数，参数为几个，则生成几个数
#randn（3，4）则会生成array



#设定直方分布图参数
bins_num = 50#五十个条条
fig, ax = plt.subplots()#画板在此
n, bins, pathes = ax.hist(x, bins_num)#normed越大，柱子越窄
plt.savefig("hist")
plt.show()#画出来的图每次也不一样

