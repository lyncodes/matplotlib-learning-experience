import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
#This module contains classes to support 
#completely configurable tick locating and formatting. 
#MaxNLocator:::Finds up to a max number of intervals with ticks at nice locations.
from collections import namedtuple
#collections是Python内建的一个集合模块
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，
#并且规定了tuple元素的个数

n_groups = 5#总共会生成5组对比

means_men = (20, 35, 30, 35, 27)#平均值
std_men = (2, 3, 4, 1, 2)#标准差

means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()#未设置参数，画出来为一张单张

index = np.arange(n_groups)
bar_width = 0.3#设置bar的宽度

opacity = 0.8#透明度
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='g',
                yerr=std_men, error_kw=error_config,
                label='Men')
#index,x coordinates of the bars,长方条的位置，可以是数字，也可使是sequence
#由于index是一个sequences，所以后面的means_men也是sequence
#bar_width，bar宽度，默认是0.8
#yerr是y方向上，的errorbar，代表不确定度，uncertainty，即标准差
#error_kw是，errorbar的绘制参数，以字典形式传入
#label用于添加图例




#画了rects1后，再执行rects2，将直接在上面继续画图
rects2 = ax.bar(index + bar_width, means_women, bar_width,
                alpha=opacity, color='r',
                yerr=std_women, error_kw=error_config,
                label='Women')
##index+bar_width,加上barwidth，正好开始紧接着画



ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width / 2)
#index+bar_width/2,将ticks们，设置在两个bar的中间，good idea啊
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
#给每一个tick这只一个名字
ax.legend()
#前面bar（）函数，label参数生成的图例，由legend函数把他们加上去

fig.tight_layout()#subplots时，将各个子图自动fit，在此处无用处
plt.savefig("barchart1.jpg")
plt.show()