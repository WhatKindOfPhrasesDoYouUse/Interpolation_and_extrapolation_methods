import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def bigData():
    n = 10
    i = np.arange(0, 2*n+1)
    VY = [1,1.05,90.6,520.4,1714.7,2915,2439.2,1020.6,230.7,32.17,
          3.29,0.3,0.03,0.004,0.001,0.0003,0.0006,0.002,0.01,0.09,0.9]
    VX = 2*math.pi*i/(2*n+1)
    #print(VX)
    XJ=[]
    scale=100
    J=0
    while J<scale:
        XJ.append(min(VX)+J*(max(VX)-min(VX))/scale)
        J=J+1
    return VY, VX, XJ

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

def fullData(x):
    VY,VX,XJ = bigData()
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

def smallData(x):
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

def chart1():
    vy, vx, xj = smallData()
    VY, VX, XJ = bigData()
    x = np.arange(0, 5.980, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, 'r*')
    lin.plot(vx, vy, 'p*')
    #lin.plot(x, fullP(x), linestyle='-', color='firebrick')
    #lin.plot(x, smallP(x), linestyle='--', color='blue')
    lin.legend(['Исходные точки', 'Триг. полн. набор', 'Триг. мал. набор'])
    lin.set_title('Сравнение тригонометрической интерполяции при полн. и мал. наборе данных')
    plt.grid()
    plt.show()

chart1()
