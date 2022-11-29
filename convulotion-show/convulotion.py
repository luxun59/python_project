#!/usr/bin/env python
# -*-coding:utf-8 -*-


'''
author: luxun
data:   2022/4/27
brief:  

'''


import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox
import numpy as np
import threading
import sys
from random import random, randrange
from time import sleep

from scipy import integrate

'''
绘制2x2的画板
可设置窗口标题和4个子图标题
可更新曲线数据
'''
quit_flag = False  # 退出标志

dt = 0.01                     #采样时间
t = np.arange(-10, 10, dt)    #时间序列

# f1 = "lambda t: np.maximum(0, 1-abs(t))"
# #f2 = lambda t: (t>0) * np.exp(-2*t)
# f2 = "lambda t: (t>0)*2*(t<1)"

class Plot2_2(object):
    """ 2x2的画板 """

    convolution=[]
    refreshFlag = True
    runFlag = True
    f1 = "lambda t: np.maximum(0, 1-abs(t))"
    f2 = "lambda t: (t>0)*2*(t<1)"

    def __init__(self, wtitle='Figure', p1title='f1', p2title='f2', p3title='f2(t-τ)',
                 p4title='convolution'):
        self.sub_title = [p1title, p2title, p3title, p4title]  # 4个子图的标题
        self.fig, self.ax = plt.subplots(2,2)  # 创建2X2子图
        self.fig.subplots_adjust(wspace=0.3, hspace=0.3)  # 设置子图之间的间距
        self.fig.canvas.set_window_title(wtitle)  # 设置窗口标题

        # 子图字典，key为子图的序号，value为子图句柄
        self.axdict = {0: self.ax[0, 0], 1: self.ax[0, 1], 2: self.ax[1, 0], 3: self.ax[1, 1]}

    def showPlot(self):
        """ 显示曲线 """

        #button
        plt.subplots_adjust(bottom=0.2)
        axprev = plt.axes([0.7, 0, 0.1, 0.075])
        axnext = plt.axes([0.81, 0, 0.1, 0.075])
        bnext = Button(axnext, 'pause')
        bnext.on_clicked(self.buttonPause)
        bprev = Button(axprev, 'start')
        bprev.on_clicked(self.buttonStart)
        #textbox
        axbox1 = plt.axes([0.1, 0.1, 0.4, 0.04])
        text_box_f1 = TextBox(axbox1, "f1")
        # text_box_f1 = TextBox(axbox1, "f1", textalignment="center")
        text_box_f1.on_submit(self.f1Submit)
        text_box_f1.set_val(self.f1[9:])

        axbox2 = plt.axes([0.1, 0.05, 0.4, 0.04])
        text_box_f2 = TextBox(axbox2, "f2")
        # text_box_f2 = TextBox(axbox2, "f2", textalignment="center")
        text_box_f2.on_submit(self.f2Submit)
        text_box_f2.set_val(self.f2[9:])

        plt.show()

    def buttonPause(self,event):
        self.runFlag = False

    def buttonStart(self,event):
        self.runFlag = True

    def f1Submit(self,expression):
        """
        Update the plotted function to the new math *expression*.

        *expression* is a string using "t" as its independent variable, e.g.
        "np.maximum(0, 1-abs(t))".
        """
        ydata = "lambda t:"+expression
        print(ydata)
        self.f1 = ydata
        self.refreshFlag  = True

    def f2Submit(self,expression):
        """
        Update the plotted function to the new math *expression*.

        *expression* is a string using "t" as its independent variable, e.g.
        "(t>0)*2*(t<1)".
        """
        ydata = "lambda t:"+expression
        print(ydata)
        self.f2 = ydata
        self.refreshFlag  = True


    def setPlotStyle(self, index):
        """ 设置子图的样式，这里仅设置了标题 """
        self.axdict[index].set_title(self.sub_title[index], fontsize=12)

    def myshift(f2,t0):
        f_shift = lambda t: f2(t0 - t)
        return f_shift

    def my_convolution(self,f1,f2,t0):
        convolution = np.zeros(len(t))
        for n, t_ in enumerate(t):
            prod = lambda tau: f1(tau) * f2(t_ - tau)
            convolution[n] = integrate.simps(prod(t), t)
        return convolution

    def updateMyPlot(self, index ,t0):
        """
        更新指定序号的子图
        :param index: 子图序号
        :return:
        """
        #实例化f1 f2
        f1 = eval(self.f1)
        f2 = eval(self.f2)

        if index < 4:
            self.axdict[index].cla()  # 清空子图数据
        if index ==0:
            self.axdict[index].plot(t, f1(t), label=r'$f_1(\tau)$')
        elif index ==1:
            self.axdict[index].plot(t, f2(t), label=r'$f_2(\tau)$')
        elif index ==2:
            f_shift = lambda t: f2(t0 - t)
            self.axdict[index].plot(t, f1(t), label=r'$f_1(\tau)$')
            self.axdict[index].plot(t, f_shift(t), label=r'$f_2shitf(\tau)$')
        elif index ==3:
            self.axdict[index].plot(t, self.convolution)
            prod = lambda tau: f1(tau) * f2(t0 - tau)
            current_value = integrate.simps(prod(t), t)
            self.axdict[index].plot(t0, current_value, 'ro')  # plot the point
        elif index==4:
            self.convolution = self.my_convolution(f1,f2,t0)

        if index < 4:
            self.setPlotStyle(index)  # 设置子图样式
            if min(t) < max(t):
                self.axdict[index].set_xlim(min(t), max(t))  # 根据X轴数据区间调整X轴范围
        plt.draw()
        print("%s end" % sys._getframe().f_code.co_name)


    def updatePlot(self, index, x, y):
        """
        更新指定序号的子图
        :param index: 子图序号
        :param x: 横轴数据
        :param y: 纵轴数据
        :return:
        """
        # X轴数据必须和Y轴数据长度一致
        if len(x) != len(y):
            ex = ValueError("x and y must have same first dimension")
            raise ex

        self.axdict[index].cla()  # 清空子图数据
        self.axdict[index].plot(x, y)  # 绘制最新的数据
        self.setPlotStyle(index)  # 设置子图样式
        if min(x) < max(x):
            self.axdict[index].set_xlim(min(x), max(x))  # 根据X轴数据区间调整X轴范围
        plt.draw()
        print("%s end" % sys._getframe().f_code.co_name)


def updatePlot(plot):
    """
    模拟收到实时数据，更新曲线的操作
    :param plot: 曲线实例
    :return:
    """
    print("Thread: %s" % threading.current_thread().getName())
    count = 0
    global quit_flag
    print("quit_flag[%s]" % str(quit_flag))

    t0=0
    

    while True:
        if quit_flag:
            print("quit_flag[%s]" % str(quit_flag))
            break

        if plot.runFlag:
            count += 1
            print("count#%d" % count)
            index = count*100 % 2000
            t0 = t[index]
            
            if plot.refreshFlag == True:
                plot.updateMyPlot(0,t0)
                plot.updateMyPlot(1,t0)
                plot.updateMyPlot(4,t0)
                # print("1111111111111111111111111111111111")
                plot.refreshFlag = False
            
            plot.updateMyPlot(2,t0)
            plot.updateMyPlot(3,t0)
        sleep(0.5)


def main():
    p = Plot2_2()  # 创建一个2X2画板

    t = threading.Thread(target=updatePlot, args=(p,))  # 启动一个线程更新曲线数据
    t.start()

    p.showPlot()  # showPlot方法会阻塞当前线程，直到窗口关闭
    print("plot close")
    global quit_flag
    quit_flag = True  # 通知更新曲线数据的线程退出

    t.join()
    print("Thread: %s end" % threading.current_thread().getName())


if __name__ == '__main__':
    main()




