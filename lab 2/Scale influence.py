import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate

def bigData():
    n = 10
    i = np.arange(0, 2*n+1)
    VY = [1,1.05,90.6,520.4,1714.7,2915,2439.2,1020.6,230.7,32.17,
          3.29,0.3,0.03,0.004,0.001,0.0003,0.0006,0.002,0.01,0.09,0.9]
    VX = 2*math.pi*i/(2*n+1)
    XJ=[]
    scale=100
    J=0
    while J<scale:
        XJ.append(min(VX)+J*(max(VX)-min(VX))/scale)
        J=J+1
    return VY, VX, XJ

# кубическая сплайн интерполяция
def cspline(x):
    VY,VX, XJ = bigData()
    C = interpolate.splrep(VX, VY)
    spl=interpolate.splev(x, C)
    return spl

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
    return XJ1,XJ2,XJ3,spl1,spl2,spl3

VY,VX,XJ = bigData()
X1,X2,X3,spl1,spl2,spl3 = scale()
x = np.arange(0,5.9,0.01)
P = interpolate.interp1d(VX, VY, kind = 2)

def chart1():
    VY, VX, XJ = bigData()
    X1, X2, X3, spl1, spl2, spl3 = scale()
    x = np.arange(0, 5.9, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(X1, spl1, linestyle='-', color='lime')
    lin.plot(X2, spl2, linestyle='-', color='violet')
    lin.plot(X3, spl3, linestyle=':', color='black')
    lin.legend(['Исходные точки', 'scale = 15', 'scale = 50', 'scale = 100'])
    lin.set_title('График влияния scale')
    plt.grid()
    plt.show()

def chart2():
    VY, VX, XJ = bigData()
    X1, X2, X3, spl1, spl2, spl3 = scale()
    x = np.arange(0, 5.9, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(X1, spl1, linestyle='-', color='lime')
    lin.plot(x, P(x), linestyle='-', color='black')
    lin.legend(['Исходные точки', 'scale = 15', 'параболическая'])
    lin.set_title('График влияния scale')
    plt.grid()
    plt.show()

def chart3():
    VY, VX, XJ = bigData()
    X1, X2, X3, spl1, spl2, spl3 = scale()
    x = np.arange(0, 5.9, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(X2, spl2, linestyle='-', color='violet')
    lin.plot(x, P(x), linestyle=':', color='black')
    lin.legend(['Исходные точки', 'scale = 50', 'параболическая'])
    lin.set_title('График влияния scale')
    plt.grid()
    plt.show()

def chart4():
    VY, VX, XJ = bigData()
    X1, X2, X3, spl1, spl2, spl3 = scale()
    x = np.arange(0, 5.9, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(X3, spl3, linestyle='-', color='red')
    lin.plot(x, P(x), linestyle=':', color='black')
    lin.legend(['Исходные точки', 'scale = 100', 'параболическая'])
    lin.set_title('График влияния scale')
    plt.grid()
    plt.show()

chart1()
chart2()
chart3()
chart4()