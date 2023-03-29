import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# полный набор данных
def bigData():
    n = 10
    i = np.arange(0, 2 * n + 1)
    VY = [1, 1.05, 90.6, 520.4, 1714.7, 2915, 2439.2, 1020.6, 230.7, 32.17,
          3.29, 0.3, 0.03, 0.004, 0.001, 0.0003, 0.0006, 0.002, 0.01, 0.09, 0.9]
    VX = 2 * math.pi * i / (2 * n + 1)
    XJ = []
    scale = 100
    J = 0
    while J < scale:
        XJ.append(min(VX) + J * (max(VX) - min(VX)) / scale)
        J = J + 1
    return VY, VX, XJ

def scale():
    VY, VX, X = bigData()
    XJ1=[]
    scale1=15
    j=0
    while j<scale1:
        XJ1.append(min(VX)+j*(max(VX)-min(VX))/scale1)
        j=j+1
    XJ2=[]
    scale2=50
    j=0
    while j<scale2:
        XJ2.append(min(VX)+j*(max(VX)-min(VX))/scale2)
        j=j+1
    XJ3=[]
    scale3=100
    j=0
    while j<scale3:
        XJ3.append(min(VX)+j*(max(VX)-min(VX))/scale3)
        j=j+1
    C = interpolate.splrep(VX, VY)
    spl1=interpolate.splev(XJ1, C)
    spl2=interpolate.splev(XJ2, C)
    spl3=interpolate.splev(XJ3, C)
    return XJ1,XJ2,XJ3,spl1,spl2,spl3

# кусочно - линейная интерполяция
def linterp(x):
    VY,VX,XJ = bigData()
    lint = np.interp(x,VX,VY)
    return lint

def cspline(x):
    VY, VX, XJ = bigData()
    C = interpolate.splrep(VX, VY)
    spl=interpolate.splev(x, C)
    return spl

x = np.arange(0, 5.980, 0.01)
VY, VX, XJ = bigData()
C = interpolate.splrep(VX, VY)
L = interpolate.splev(x, C) # линейная
P = interpolate.interp1d(VX, VY, kind = 2) # параболическая
S = interpolate.interp1d(VX, VY, kind = 3) # кубическая

# график кусочно - линейной интерполяции (1 по тз)
def chart1():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, linterp(x), '-b')
    lin.legend(['Исходные точки', 'Кусочно-линейная интерполяция'])
    lin.set_title('Кусочно - линейная интерполяция')
    plt.grid()
    plt.show()

# график сравнения кусочно - линейной и сплайн - линейной интерполяции
def chart2():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, linterp(x), '-b')
    lin.plot(x, L, linestyle = '--', color ='green')
    lin.legend(['Исходные точки', 'Кусочно-линейная интерполяция', 'Сплайн-линейная'])
    lin.set_title('Сравнение кусочно - линейной и сплайн - линейной')
    plt.grid()
    plt.show()

# график сплайн интерполяций
def chart3():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, L, linestyle = "-", color = 'blue')
    lin.plot(x, S(x), linestyle = '--', color = 'green')
    lin.plot(x, P(x), linestyle = ':', color = 'pink')
    lin.legend(['Исходные точки', 'Линейная', 'Кубическая', 'Параболическая'])
    lin.set_title('Сравнение сплайн интерполяций')
    plt.grid()
    plt.show()

# график сравнения интерполяций вне диапазона
def chart4():
    VY, VX, XJ = bigData()
    x = np.arange(-0.5, 9, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, linterp(x), '-g')
    lin.plot(x, cspline(x), linestyle = ':', color = 'blue')
    lin.legend(['Исходные точки', 'Линейная интерполяция', 'Сплайн линейная'])
    lin.set_title('Сравнение интерполяции вне диапазона')
    plt.grid()
    plt.show()

chart1()
chart2()
chart3()
chart4()

