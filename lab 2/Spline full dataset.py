import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
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
    VY,VX,X=bigData()
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
    return XJ1,XJ2,XJ3,spl1,spl2,

# кусочно - линейная интерполяция
def piecewiseLinearInterpolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='linear')
    return f(x)

# сплайн - линейная интерполяция
def splineLinearInterpolation(x):
    VY, VX, XJ = bigData()
    C = interpolate.splrep(VX, VY)
    f = interpolate.splev(x, C)
    return f

# сплайн - кубическая интерполяция
def splineCubicInterpolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY,'cubic')
    return f(x)

# сплайн - пабаробилческая интерполяция
def splineParabolicInterpolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='quadratic')
    return f(x)

# кусочно - линейная экстраполяция
def piecewiseLinearExtrapolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='linear', fill_value='extrapolate')
    return f(x)

# сплайн - кубическая экстрополяция
def splineCubicExtrapolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY,'cubic', fill_value='extrapolate')
    return f(x)

# сплайн - параболическая экстрополяция
def splineParabolicExtrapolation(x):
    VY, VX, XJ = bigData()
    f = interpolate.interp1d(VX, VY, kind='quadratic', fill_value='extrapolate')
    return f(x)

# сплайн - линейная экстрополяця
def cspline(x):
    VY, VX, XJ = bigData()
    C = interpolate.splrep(VX, VY)
    spl=interpolate.splev(x, C)
    return spl

# график кусочно - линейной интерполяции
def chart1():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, piecewiseLinearInterpolation(x), '-b')
    lin.legend(['Исходные точки', 'Кусочно - линейная интерполяция'])
    lin.set_title('Кусочно - линейная интерполяция')
    plt.grid()
    plt.show()

# график сравнения кусочно - линейной и сплайн - линейной интерполяции
def chart2():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, piecewiseLinearInterpolation(x), '-b')
    lin.plot(x, splineLinearInterpolation(x), '-g')
    lin.legend(['Исходные точки', 'Кусочно - линеная', 'Сплайн - линейная'])
    lin.set_title('Cравнения кусочно - линейной и сплайн - линейной интерполяции')
    plt.grid()
    plt.show()

# сравнение 3 видов сплайн интерполяции
def chart3():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, splineLinearInterpolation(x), '--b')
    lin.plot(x, splineParabolicInterpolation(x), ':g')
    lin.plot(x, splineCubicInterpolation(x), ':y')
    lin.legend(['Исходные точки', 'Линейная', 'Кубическая', 'Параболическая'])
    lin.set_title('Сравнение сплайн интерполяций')
    plt.grid()
    plt.show()

# сравнение 3 видов сплайн интерполяции на изгибе
def chart4():
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, splineLinearInterpolation(x), '--b')
    lin.plot(x, splineParabolicInterpolation(x), ':g')
    lin.plot(x, splineCubicInterpolation(x), '-y')
    plt.xlim(0, 0.7)
    plt.ylim(-50, 100)
    lin.legend(['Исходные точки', 'Линейная', 'Кубическая', 'Параболическая'])
    lin.set_title('Сравнение сплайн интерполяций на изгибе')
    plt.grid()
    plt.show()

# график интерполяции вне диапазона
def chart5():
    VY, VX, XJ = bigData()
    x = np.arange(5, 8, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, piecewiseLinearExtrapolation(x), '-g')
    lin.plot(x, splineCubicExtrapolation(x), '-b')
    lin.plot(x, splineParabolicExtrapolation(x), '-y')
    plt.xlim(5, 8)
    plt.ylim(-5, 25)
    lin.legend(['Исходные точки','Сплайн - кубическая', 'Сплайн - линейная', 'Сплайн - параболическая'])
    lin.set_title('Экстраполяция')
    plt.grid()
    plt.show()

# вычисление значений в узле и между узлами
def calculationsNode():
    print("Интерполяция в узле (0.299199)")
    print("Кусочно - линеная: ", piecewiseLinearInterpolation(0.299199))
    print("Сплайн - линейная: ", splineLinearInterpolation(0.299199))
    print("Сплайн - кубическая: ", splineCubicInterpolation(0.299199))
    print("Сплайн - параболическая: ", splineParabolicInterpolation(0.299199))
    print("Интерполяция между узлами (1.6)")
    print("Кусочно - линейная: ", piecewiseLinearInterpolation(1.6))
    print("Сплайн - линейная: ", splineLinearInterpolation(1.6))
    print("Сплайн - кубическая: ", splineCubicInterpolation(1.6))
    print("Сплайн - параболическая: ", splineParabolicInterpolation(1.6))
    return

#chart1()
#chart2()
#chart3()
#chart4()
#chart5()
#chart6()
#calculationsNode()
