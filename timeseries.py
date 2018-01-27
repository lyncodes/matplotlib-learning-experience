import datetime
'''
The datetime module supplies classes for 
manipulating dates and times in both simple
 and complex ways
'''
import numpy as np
import matplotlib.pyplot as plt
'''
matplotlib.pyplot is a state-based interface 
to matplotlib. It provides a MATLAB-like way 
of plotting.
'''
import matplotlib.dates as mdates
'''
Matplotlib provides sophisticated date plotting
 capabilities, standing on the shoulders of
  python datetime
'''
import matplotlib.cbook as cbook
'''
A collection of utility functions and classes
'''
years = mdates.YearLocator()
#在每一年的一月一号做tick
months = mdates.MonthLocator()
#给每一个月都做上tick
yearsFmt = mdates.DateFormatter('%Y')#按年份设置时间格式，此处精确到年份，最多可以精确到秒


# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
with cbook.get_sample_data('goog.npz') as datafile:
	#NPZ file is a NumPy Zipped Data
    r = np.load(datafile)['price_data'].view(np.recarray)
# Matplotlib works better with datetime.datetime than np.datetime64, but the
# latter is more portable.
date = r.date.astype('O')

fig, ax = plt.subplots()
ax.plot(date, r.adj_close)####此时股价的图片已经画好了

# plt.show()
# exit()


# format the ticks
ax.xaxis.set_major_locator(years)#主要刻度精度
ax.xaxis.set_major_formatter(yearsFmt)#主要刻度的单位
ax.xaxis.set_minor_locator(months)#次要刻度精度

datemin = datetime.date(date.min().year, 1, 1)
#date函数，三个参数分别是年月日，返回一个date类型的object，代表时间
datemax = datetime.date(date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)#设置图画的x limitation


# format the coords message box
def price(x):
    return '$%1.2f' % x
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = price
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()
#autofmt_xdate（）函数，用来自动分配ticklabels，免得各个ticlabels重叠

plt.title("the price")
plt.savefig("timeseries.jpg")
plt.show()





