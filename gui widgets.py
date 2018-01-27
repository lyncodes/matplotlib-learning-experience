import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
#slider是滑块选项，button用于设置reset


# RadioButton 控件为用户提供由两个或多个互斥选项组成的选项集
#即是左侧的red、blue、green三个选项

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0*np.sin(2*np.pi*f0*t)#三角函数标准表达式Asin(wx+fai)


l, = plt.plot(t, s, lw=1, color='red')#lw is linewodth
####为什么l后面要跟一个空格呢？？


plt.axis([0, 1, -10, 10])

axcolor = 'g'#slider的颜色
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
#facecolor is background color
#rect = [left, bottom, width, height] 
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)#f0,a0是初始位置
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
#两个数字数slider的左右界限
#valinit是silde的初始位置

def update(val):#这个update用于，silder移动的时候，向绘图函数实时update参数
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()

sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])#设置reset buttom的位置
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.95')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)#设置radiobuttom
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()


radio.on_clicked(colorfunc)


plt.savefig("gui widgets.jpg")
plt.show()