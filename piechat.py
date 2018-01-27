import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#默认是逆时针方向
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]#总共加起来100
explode = (0, 2, 0, 1)  #非零数字越大，扇形离圆心就越远
# only "explode" the 2nd slice (i.e. 'Hogs')，作为特别标记

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, radius=15)
# autopct用于给各个扇形加上数字标签，显示具体份额
#label the wedges with their numeric value

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("piechart.jpg")
plt.show()