"""
Interpolation.py
Author: Juan Cruz
4-2-14

This program creates Langrange and Hermite
Interpolating Polynomials as well as piecewise
linear and cubic spline interpolating functions.
This Program shall also produce graphs, each of which
shows the graph of f(x) and one interpolant.

"""
import math

m400group = 5
m400names = ['Juan Cruz']

def printNames():
    print("Interpolation.py by %s:"%(m400group)),
    for name in m400names:
        print("%s, "%(name)),
    print
    
printNames()

#Reverses a generic array array
def reverse(L):
    R = []
    for i in range(len(L)-1,-1,-1):
        R.append(L[i])
    return(R)

def printPoly(P):
    for i in reverse(range(len(P))):
        try:
            if len(P[i]) == 2 :
                if P[i][1] !=0:
                    if P[i][0] != 1:
                        print("%s x^%s + "%(P[i][0], P[i][1])),
                    else:
                        print("x^%s + "%(P[i][1])),
                else:
                    print("%s +"%(P[i][0])),                
            else:
                print("Wrong Number of Args for inner list"),
        except:
            if P[i] != 0:
                if i != 0:
                    if P[i] != 1:
                        print("%s x^%s + "%(P[i], i)),
                    else:
                        print("x^%s + "%(i)),
                else:
                    print("%s"%(P[i])),
    print

#Prints a spline section with a given data
def printSpline(func, data):
    for i in range(len(func)):
        printPoly(func[i])
        print("for %.2f <= X <= %.2f \n" % (data[i][0],data[i+1][0]))


def showMatrix(mat):
    for row in mat:
        print(row)
    
def getCol(mat, col):
    r = len(mat)
    columVec = []
    for i in range(r):
        columVec.append(mat[i][col]),
    return(columVec)

#adds 2 Polynomials to one. Both Polys Must be same size
def addPoly(S,T):
    ST =[]
    for i in range(len(S)):
        ST.append( S[i] +T[i] )
    return(ST)

#adds 2 Polynomials that can differ in length
def addPoly2(P1, P2):
    Result = []
    l1 = len(P1)
    l2 = len(P2)
    if l1<l2:
        for i in range(l2):
            if i < l1:
                Result.append(P1[i] + P2[i])
            else:
                Result.append(P2[i])
    else:
        for i in range(l1):
            if i < l2:
                Result.append(P1[i] + P2[i])
            else:
                Result.append(P1[i])
    return Result

def scalPoly(s,V):
    sV = []
    for i in V:
        sV.append(s*i)
    return(sV) 

def multPoly(p1, p2):
    p1Len = len(p1)
    p2Len = len(p2)
    result = [0] *( p1Len + p2Len -1 )

    for i in range(p1Len):
        for j in range(p2Len):
            result[i+j] = p1[i]*p2[j] + result[i+j]
    return result

#evaluates a given polynomial(array format) at a certain x value.
def evalPoly(P,x):
    result = 0;
    for i in range(len(P)):
        result = result + P[i]*(x**i)
    return result

#Random Equation for testing purposes. Function returns value at a given x.
def F(x):
    return ( (1.6*math.e**(-2*x))*(math.sin(3*math.pi*x)) )

#derivative Equation of F(X)
def Fd(x):
    return (math.e**(-2.0*x))*(4.8*math.pi*math.cos(3.0*math.pi*x) - 3.2*math.sin(3.0*math.pi*x) )

#Function returns ordered data given x interval on the function F(X). For test purposes
def GetData(X):
    data = []
    for i in range(len(X)):
        temp = [X[i], F(X[i]),Fd(X[i])]
        data.append(temp)
    return data

#Finding Kth term Langrange coefficient
def LK(k, data):
    result = [1]
    denom = 1
    Xk = data[k][0]
    for i in range(len(data)):
        if i!=k:
            result = multPoly( result, [(-1.0)*data[i][0], 1] )
            denom = denom*(Xk - data[i][0])

    result = scalPoly(1.0/denom, result)
    return result

#finding Nth term Hermite Coefficient
def HCo(n , data):
    n = n-1
    Z = [0]*(2*n+2)
    Q = []
    for i in range(2*n+2):
        Q.append([0]*(2*n+2))
    for i in range(n+1):
        XI = data[i][0]
        FXI = data[i][1]
        FDXI = data[i][2]
        twoI = 2*i
        Z[twoI] = XI
        Z[twoI +1] = XI
        Q[twoI][0] = FXI
        Q[twoI+1][0] = FXI
        Q[twoI+1][1] = FDXI    
        if i != 0:
            Q[2*i][1] = ( Q[twoI][0]-Q[twoI-1][0] )/ ( Z[twoI] -Z[twoI-1] )     
    for i in range(2, 2*n+2):
        for j in range(2, i+1):
            Q[i][j] = ( Q[i][j-1]-Q[i-1][j-1] )/ (Z[i]-Z[i-j])
    Result = []
    for i in range(len(Q)):
        Result.append(Q[i][i])
    return Result

#Finds Linear Splines
def LS(data, i):
    slope = (1.0*data[i+1][1]-data[i][1])/(data[i+1][0]-data[i][0])
    result = scalPoly(slope, [(-1.0)*data[i][0], 1])
    result = addPoly2(result, [data[i][1]])
    return result

#Finds Cubic Linear Splines
def CS(data):
    n = len(data)-1
    x = getCol(data,0)
    h = [0]*(n)
    alpha = [0]*(n+1)
    l = [0]*(n+1)
    m = [0]*(n+1)
    z = [0]*(n+1)

    a = getCol(data,1)
    b = [0]*(n+1)
    c = [0]*(n+1)
    d = [0]*(n+1)
    
    FPO = data[0][2]
    FPN = data[n][2]

    "step 1 --- imax == n-1"
    for i in range(n):                    
        h[i] = x[i+1] - x[i]
        
    "step 2"
    alpha[0] = ( 3*(a[1] -a[0]) )/h[0] - 3*FPO    
    alpha[n] = 3*FPN - 3*(a[n]-a[n-1])/h[n-1]
    "step 3 --- imax == n-1"
    for i in range(1,n):                  
        alpha[i] = (3.0/h[i])*(a[i+1]-a[i]) - (3.0/h[i-1])*(a[i]-a[i-1])

    "step 4"
    l[0] = 2.0*h[0]
    m[0] = 0.5
    z[0] = ((1.0)*alpha[0])/l[0]

    "step 5 --- imax == n-1"
    for i in range(1,n):
        l[i] = 2.0*(x[i+1] - x[i-1]) - h[i-1]*m[i-1]
        m[i] = ((1.0)*h[i])/l[i]
        z[i] = (alpha[i]-((1.0)*h[i-1]*z[i-1]) )/l[i]
        
    "step 6"
    l[n] = h[n-1]*(2-m[n-1])
    z[n] = (1.0*alpha[n]-h[n-1]*z[n-1])/l[n]
    c[n] = z[n]

    "step 7"
    j = n-1

    while j>=0:
        c[j] = z[j]-m[j]*c[j+1]
        b[j] = ((1.0)*a[j+1]-a[j])/h[j] - h[j]*(c[j+1]+2.0*c[j])/3.0
        d[j] = (c[j+1]-c[j])/(3.0*h[j])
        j = j-1
    result = []
    result.append(a)
    result.append(b)
    result.append(c)
    result.append(d)
    return result

#Finding Hermite Coefficients
def HFac(size, X):
    Hf = [[1]]
    k = 0
    for i in range(1,size):
        T = multPoly(Hf[i-1], [(-1)*X[k], 1])
        Hf.append(T)
        if i %2 ==0:
            k = k+1
    return Hf

#Returns Langrange Polynomial 
def LPoly(n, data):
    Poly = []
    for i in range(n):
        tempPoly = LK(i,data)
        tempPoly = scalPoly(data[i][1], tempPoly)
        Poly.append(tempPoly)

    Result = [0]*len(Poly[0])      
    for i in range(len(Poly)):
        Result = addPoly(Result,Poly[i])
    return Result

#Returns Hermite Polynomials
def HPoly(HC, HF):    
    TResult = []
    Result = [0]
    for i in range(len(HF)):
        T = scalPoly(HC[i], HF[i])
        TResult.append(T)
    for i in range(len(TResult)):
        Result = addPoly2(Result, TResult[i])
    return Result

#Returns Line Spline functions
def LinSpline(data):
    ls = []
    for i in range(len(data)-1):
        ls.append(LS(data, i))
    return ls

#Returning Cubic Spline functions
def CubicSpline(data):
    cs = CS(data)
    ResultS = []
    X = getCol(data,0)
    
    for i in range(len(data)-1):
        polySum = [0]
        tempPoly = [1]
        for j in range(4):
            polySum = addPoly2(polySum, scalPoly(cs[j][i],tempPoly))
            tempPoly = multPoly(tempPoly, [(-1.0*X[i]), 1])
        ResultS.append(polySum)
    return ResultS

#Langrange Method
def LMethod(data):
    LP = LPoly(len(data), data)
    return LP
#Hermite Method
def HMethod(data):
    HC = HCo(len(data), data)
    HF = HFac(len(HC), getCol(data,0))
    HP = HPoly(HC,HF)
    return HP
#Linear Spline Method
def LSMethod(data):
    ls = LinSpline(data)
    return ls

def LSMethod2(data, num):
    ls = LinSpline(data)
    k = -1
    for i in range(1,len(data)):
        if (num >= data[i-1][0]) and (num <= data[i][0]):
            k = i-1
            break
    if k >= 0:
        result = evalPoly(ls[k], num)
        printSpline(ls, data)
        print("LS(%.2f) = %f\n" % (num, result))
    else:
        print("\nError, Cannot compute Linear Spline. %f is not within Xo and Xn.\n" %(num))
    return ls

#Cubic Spline Method
def CSMethod(data):
    S = CubicSpline(data)
    return S

def CSMethod2(data, num):
    S = CubicSpline(data)
    k = -1
    for i in range(1,len(data)):
        if (num >= data[i-1][0]) and (num <= data[i][0]):
            k = i-1
            break
    if k >= 0:
        result = evalPoly(S[k], num)
        printSpline(S, data)
        print("S(%.2f) = %f\n" % (num, result))
    else:
        print("\nError, Cannot compute Linear Spline. %f is not within Xo and Xn.\n" %(num))
    return S

def lam(data):
    result = [1]
    for i in range(len(data)):
        result = multPoly(result,[(-1.0)*data[i][0], 1])
    return result

####Testing Area####
print("-----------------Testing---------------------")
d = [[2,0.5],[2.5,0.4],[4,0.25]]
r = LMethod(d)
print("\nLangrange Method Example 1:\nOn Data :")
showMatrix(d)
print "\nLangrange P(x) = "
printPoly(r)
print("P(3) = %f \n"% (evalPoly(r,3)))

print("##############################################")

d2 = [[1.3,.6200860,-0.5220232],[1.6,0.4554022,-0.5698959],[1.9,0.2818186,-0.5811571]]
r2 = HMethod(d2)
print("\nHermite Method Example 2:\nOn Data :")
showMatrix(d2)
print "\nHermite P(x) = "
printPoly(r2)
print("P(1.5) = %f \n"% (evalPoly(r2,1.5)))

print("##############################################")

print("\nLinear Spline Method Example :\nOn Data :")
d3 = [[0,0],[10,227.04],[15,362.78],[20,517.35],[22.5,602.97]]
showMatrix(d3)
print "\nLinear Spline LS(x) = "
ls = LSMethod2(d3, 16)

print("##############################################")

print("\nCubic Spline Example:\nOn Data :")
d4 = [[0,1, 1],[1, math.e, math.e],[2, math.e**2, math.e**2],[3, math.e**3, math.e**3]]
showMatrix(d4)
print "\nCubic Spline CS(X) = "
cs = CSMethod2(d4, 1.0/3)

print("-----------------End Test---------------------")

######Interpolating one data set using all methods ######
print("\n******** Interpolating data using Langrange, Hermite, Linear Spline, and Cubic Spline *********\n")
d4 = GetData( [0, 1.0/6, 1.0/3, 1.0/2, 7.0/12, 2.0/3, 3.0/4, 5.0/6, 11.0/12, 1.0] )
print("On Data Set :\nXi\tF(Xi)\t\tF'(Xi)\t\tGiven by F(X) = 1.6*e^(-2*x)*sin(3*pi*x)")

showMatrix(d4)

#Langrange Method
lp = LMethod(d4)
print "\nLangrange P(x) = "
printPoly(lp)
print("P(0.58) = %f \n"% (evalPoly(lp,7.0/12)))

#Hermite Method
hp = HMethod(d4)
print "\nHermite P(x) = "
printPoly(hp)
print("P(0.58) = %f \n"% (evalPoly(hp,7.0/12)))

#Linear Spline Method
print "\nLinear Spline LS(x) = "
ls = LSMethod2(d4, 7.0/12)

#Cubic Spline Method
print "\nCubic Spline CS(x) = "
ls = CSMethod2(d4, 7.0/12)
