"""
plotInterp.py
Autor: Juan Cruz
4-2-14

This program creates Langrange and Hermite
Interpolating Polynomials as well as piecewise
linear and cubic spline interpolating functions.
This Program shall also produce graphs, each of which
shows the graph of f(x) and one interpolant.

"""

#importring interpolation.py so we can  use some functions
import interpolation

import matplotlib.pyplot as plt
from numpy import arange
from math import *

xInterval = [0, 1.0/6, 1.0/3, 1.0/2, 7.0/12, 2.0/3, 3.0/4, 5.0/6, 11.0/12, 1.0]
#import data set and Polynomials
"iData contains data points for specific X's on a specific function"
iData = interpolation.GetData(xInterval)

LR = interpolation.LMethod(iData)
HR = interpolation.HMethod(iData)
LSR = interpolation.LSMethod(iData)
CSR = interpolation.CSMethod(iData)

#import data for Multiple Graphs for L6(X) and PI(X)
multLsix = []
multPie = []

td1 = interpolation.GetData( [0.0, 1.0/6, 1.0/3, 1.0/2, 7.0/12, 2.0/3,  5.0/6, 1.0] )
td2 = interpolation.GetData( [1.0/6, 1.0/3, 1.0/2,  7.0/12, 2.0/3, 5.0/6, 11.0/12, 1.0] )
td3 = interpolation.GetData( [0.0, 1.0/6, 1.0/2, 7.0/12, 2.0/3, 3.0/4, 5.0/6, 11.0/12, 1.0] )

td = [td1,td2,td3, iData]
for i in range(len(td)):
    multLsix.append(interpolation.LK(6,td[i]))
    multPie.append(interpolation.lam(td[i]))

#Domain for graphs
delta = .01
interval = arange(-1.2, 2.2, delta)

#Plots for each Graph and Interpolating functions
def showF():
    #Y's for F(Xi)
    FXI = [interpolation.F(t) for t in interval]

    #Ploting F(X)
    plt.plot(interval, FXI, color="blue", label = r'$F(x)$')

def showLan():
    #Y's for Lan(X)
    LFunc = LR
    LY  = [interpolation.evalPoly(LFunc,t) for t in interval]
    
    #plot graph
    plt.plot(interval, LY, color="red", label = r'$Langrange P(x)$')

def showHerm():
    #Y's for Herm(X)
    HFunc = HR
    HY = [interpolation.evalPoly(HFunc,t) for t in interval]

    #plot graph
    plt.plot(interval, HY, color="green", label = r'$Hermite P(x)$')

def getSplineY(S, data, num):
    k = -1
    for i in range(1,len(data)):
        if (num >= data[i-1][0]) and (num <= data[i][0]):
            k = i-1
            break
    if k>=0:
        return interpolation.evalPoly(S[k], num)
    else:
        return interpolation.F(num)
    
def showLinSpline():
    #imported data
    LS = LSR
    data = iData
    #Y's for Linear Spline
    tInterval = arange(data[0][0],data[len(data)-1][0], delta)
    LSY = [getSplineY(LS, data, t) for t in tInterval]
    
    plt.plot(tInterval, LSY, color ="purple", label = r'$Linear Spline S(x)$')

def showCubicSpline():
    S = CSR
    data = iData
    #Y's for Cubic Spline
    tInterval = arange(data[0][0],data[len(data)-1][0], delta)
    SY = [getSplineY(S, data, t) for t in tInterval]

    plt.plot(tInterval, SY, color="orange", label = r'$Cubic Spline S(x)$')
    
def showLsixes():
    mat = multLsix

    for i in range(len(mat)):
        matY = [interpolation.evalPoly(mat[i], t) for t in interval]
        plt.plot(interval, matY, label = ("L6(X)-%i" %(i)) )
        
    #Change Axis
    plt.axis([-0.6, 1.6, -5, 5], 'equal')

    #put horizontal and vertical lines for Axis
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    # legen of the two plots in lower right hand corner
    plt.legend(loc='lower right')
    
    #save plot
    plt.show()
    #plt.savefig("Fx.svg")
    plt.savefig("fx.png")

def showPies():
    mat = multPie
    data = iData
    for i in range(len(mat)):
        matY = [interpolation.evalPoly(mat[i], t) for t in interval]
        plt.plot(interval, matY, label = ("PI(X)-%i" %(i)) )

    #Change Axis
    plt.axis([-3.6, 3.6, -10, 10], 'equal')

    #put horizontal and vertical lines for Axis
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    # legen of the two plots in lower right hand corner
    plt.legend(loc='lower right')
    
    #save plot
    plt.show()
    #plt.savefig("Fx.svg")
    plt.savefig("fx.png")


def plotAll():
    showF()
    showLan()
    showLinSpline()
    showCubicSpline()
    restConfig()
    

def restConfig():
    padx = .1
    pady = .1
    a = min(xInterval)
    b = max(xInterval)
    yResults = [interpolation.F(t) for t in xInterval]
    minY = min(yResults)
    maxY = max(yResults)

    #Config Axis
    plt.axis([a-padx, b+padx, minY-pady, maxY+pady], 'equal')

    #put horizontal and vertical lines for Axis
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    # legen of the two plots in lower right hand corner
    plt.legend(loc='lower right')
    
    #save plot
    plt.show()
    #plt.savefig("Fx.svg")
    plt.savefig("fx.png")

print("\nPlotting Corresponding Graphs...\n")
plotAll()
