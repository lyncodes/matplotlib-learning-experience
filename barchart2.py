import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
#ticker模块用于设定刻度的位置和格式
#maxnlocator，找出ticks的最大个数
#
from collections import namedtuple
#namedtple创建一个和tuple类似的对象，而且对象可访问

#namedtple创建一个和tuple类似的对象，而且对象可访问
Student = namedtuple('Student', ['name', 'grade', 'gender'])


Score = namedtuple('Score', ['score', 'percentile'])

# GLOBAL CONSTANTS
testNames = ['Pacer Test', 'Flexed Arm\nHang', 'Mile Run', 'Agility',
             'Push Ups']
testMeta = dict(zip(testNames, ['laps', 'sec', 'min:sec', 'sec', '']))
#zip()函数，将两组sequence进行一一对应的封装
#见图中左右对应的测试项目和测试成绩对应的单位

def attach_ordinal(num):#给名次加上英文后缀
    """helper function to add ordinal string to integers

    1 -> 1st
    56 -> 56th
    """
    #ordinal序数的，排序的

    suffixes = dict((str(i), v) for i, v in#这里是for的多变量循环
                    enumerate(['th', 'st', 'nd', 'rd', 'th',
                               'th', 'th', 'th', 'th', 'th']))
    #print(suffixes),将会输出
    #{'0': 'th', '1': 'st', '2': 'nd', '3': 'rd', 
    #'4': 'th', '5': 'th', '6': 'th', '7': 'th',
    # '8': 'th', '9': 'th'}，这是一个末尾数字和相应的字母对应的字典
    #0 1 2 3 4 5 6 7 8 9，分别是enumerate（）函数自己产生的index数字
    #str（i）函数，把数字1-0，也转换成为string。再封装成为dictionary

    

    #给排名添加上后缀

    v = str(num)#将正儿八经的排名数字转换为str
    # special case early teens
    if v in {'11', '12', '13'}:
        return v + 'th'#英语语法，teens的年龄，11-13，加th
    return v + suffixes[v[-1]]#此时的v是一个str，从后面引用v的最后一个字符，得到末尾数字


def format_score(scr, test):#添加成绩标签，laps or seconds，或者没有标签

    #scr为返回的成绩数字，test为成绩的类型

    """
    Build up the score labels for the right Y-axis by first
    appending a carriage return to each string and then tacking on
    the appropriate meta information (i.e., 'laps' vs 'seconds'). We
    want the labels centered on the ticks, so if there is no meta
    info (like for pushups) then don't add the carriage return to
    the string
    """
    md = testMeta[test]
    #print(testMeta)
    #testMeta长这个样子，{'Pacer Test': 'laps', 'Flexed Arm Hang': 'sec',
    # 'Mile Run': 'min:sec', 'Agility': 'sec', 'Push Ups': ''}，一个字典

    if md:
        return '{0}\n{1}'.format(scr, md)#md就是分数score的单位
    else:
        return scr#score没有单位的时候，就直接返回其值

def format_ycursor(y):#提供y参数，y是测试项目的数量，返回相应的测试项目名称
    y = int(y)
    if y < 0 or y >= len(testNames):
        return ''
    else:
        return testNames[y]


def plot_student_results(student, scores, cohort_size):
    #对最终结果进行绘图
    #  create the figure
    fig, ax1 = plt.subplots(figsize=(8, 5))#设置图片大小,ax1只有一张子图

    pos = np.arange(len(testNames))#由testName的容量大小，设定pos的位置
    #pos用于精确放置标签位置

    rects = ax1.barh(pos, [scores[k].percentile for k in testNames],
                     align='center',
                     height=0.5, color='b',
                     tick_label=testNames)
    #[scores[k].percentile for k in testNames]是数据来源

    ax1.set_title(student.name)#学生的名字，再后面会传入参数

    ax1.set_xlim([0, 100])#设定x轴的最大值
    ax1.xaxis.set_major_locator(MaxNLocator(11))#MaxNLocator设定ticks的最大个数
    
    ax1.xaxis.grid(True, linestyle='--', which='major',
                   color='r', alpha=.5)#图片网格的相关设置，gridline
    # Plot a solid vertical gridline to highlight the median position

    ax1.axvline(50, color='grey', alpha=0.25)
    # set X-axis tick marks at the deciles
    cohort_label = ax1.text(.5, -.07, 'Cohort Size: {0}'.format(cohort_size),
                            horizontalalignment='center', size='small',
                            transform=ax1.transAxes)



    # Set the right-hand Y-axis ticks and labels
    ax2 = ax1.twinx()#Create a twin Axes sharing the xaxis，建立第二个坐标轴

    scoreLabels = [format_score(scores[k].score, k) for k in testNames]
    #调用前面的format_score()函数，生成成绩标签，k是成绩项目的名字，

    # set the tick locations
    ax2.set_yticks(pos)#pos是位置
    # make sure that the limits are set equally on both yaxis so the
    # ticks line up
    ax2.set_ylim(ax1.get_ylim())
    #get_ylim()自动返回y轴的界限所在，as the tuple (bottom, top).



    # set the tick labels
    ax2.set_yticklabels(scoreLabels)#116行处，scorelabels是已经生成的成绩标签，现在将其放上图片

    ax2.set_ylabel('Test Scores')

    ax2.set_xlabel(('Percentile Ranking Across '
                    '{grade} Grade {gender}s').format(
                        grade=attach_ordinal(student.grade),
                        gender=student.gender.title()))

    rect_labels = []
    # Lastly, write in the ranking inside each bar to aid in interpretation
    for rect in rects:
        # Rectangle widths are already integer-valued but are floating
        # type, so it helps to remove the trailing decimal point and 0 by
        # converting width to int type
        width = int(rect.get_width())

        rankStr = attach_ordinal(width)
        # The bars aren't wide enough to print the ranking inside
        if (width < 5):
            # Shift the text to the right side of the right edge
            xloc = width + 1
            # Black against white background
            clr = 'black'
            align = 'left'
        else:
            # Shift the text to the left side of the right edge
            xloc = 0.98*width
            # White on magenta
            clr = 'white'
            align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height()/2.0
        label = ax1.text(xloc, yloc, rankStr, horizontalalignment=align,
                         verticalalignment='center', color=clr, weight='bold',
                         clip_on=True)
        rect_labels.append(label)

    # make the interactive mouse over give the bar title
    ax2.fmt_ydata = format_ycursor
    # return all of the artists created
    return {'fig': fig,
            'ax': ax1,
            'ax_right': ax2,
            'bars': rects,
            'perc_labels': rect_labels,
            'cohort_label': cohort_label}

student = Student('Johnny Doe', 2, 'boy')#对前面的namedtuple进行初始化
scores = dict(zip(testNames,(Score(v, p) 
    for v, p in zip(['7', '48', '12:52', '17', '14'],#这个是成绩，绝对成绩
        np.round(np.random.uniform(0, 1,len(testNames))*100, 0)))))
cohort_size = 62  # The number of other 2nd grade boys
#总参加测试人数

arts = plot_student_results(student, scores, cohort_size)#调用绘图函数
#student是一个用tuple初始化好的tuple


plt.savefig("barchart2.jpg")
plt.show()