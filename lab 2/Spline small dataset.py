import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate

def smallData():
    vy = [1,90.6,1714.7,2439.2,230.7,3.29,0.03,0.001,0.0006,0.01,0.9]
    vx = [0, 0.598399, 1.196797, 1.795196, 2.393594, 2.991993, 3.590392,
          4.18879, 4.787189, 5.385587, 5.983986]
    xj=[]
    scale=100
    j=0
    while j<scale:
        xj.append(min(vx)+j*(max(vx)-min(vx))/scale)
        j=j+1
    return vy, vx, xj

# кусочно - линейная интерполяция
def linterp(x):
    VY,VX,XJ = smallData()
    lint = np.interp(x,VX,VY)
    return lint

def cspline(x):
    VY, VX, XJ = smallData()
    C = interpolate.splrep(VX, VY)
    spl=interpolate.splev(x, C)
    return spl

def P(x):
    VY,VX,XJ = smallData()
    n=10
    i=0
    a0=0
    while i < 2*n+1:
        a0+=VY[i]
        i=i+1
    a0=a0/(2*n+1)
    k=1
    ak=[]
    bk=[]
    while k<n+1:
        a=b=0
        i=0
        while i<2*n+1:
            a+=VY[i]*math.cos(k*VX[i])
            b+=VY[i]*math.sin(k*VX[i])
            i=i+1
        ak.append(a/(2*n+1))
        bk.append(b/(2*n+1))
        k=k+1
    i=0
    c=[]
    c1=[]
    while i<len(x):
        p=0
        p1=0
        k=1
        k1=0
        while k<n+1:
            p+=ak[k1]*math.cos(k*x[i])
            p1+=bk[k1]*math.sin(k*x[i])
            k=k+1
            k1=k1+1
        c.append(p)
        c1.append(p1)
        i=i+1
    k=0
    P=[]
    while k<len(c):
        P.append((c[k]+c1[k])*2+a0)
        k=k+1
    return P

x = np.arange(0, 5.980, 0.01)
VY, VX, XJ = smallData()
C = interpolate.splrep(VX, VY)
L = interpolate.splev(x, C) # линейная
P = interpolate.interp1d(VX, VY, kind = 2) # параболическая
S = interpolate.interp1d(VX, VY, kind = 3) # кубическая


def chart1():
    VY, VX, XJ = smallData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(x, P(x), linestyle='-', color='firebrick')
    lin.legend(['Исходные точки', 'Тригонометрическая интерполяция'])
    lin.set_title('График тригонометрической интерполяции')
    plt.grid()
    plt.show()

chart1()

