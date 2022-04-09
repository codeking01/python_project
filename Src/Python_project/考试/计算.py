import math
import warnings
from fractions import Fraction
from math import e

import numpy as np
from numpy import sin
from scipy import integrate
from scipy.optimize import curve_fit
from sympy import ln, dsolve, Eq
from sympy import sin
from sympy import *

if __name__ == '__main__':
    # x, y, z = sympy.symbols('x y z')
    # try:
    #     result = sympy.solve([x + 5 * y ** 2 + z - 3, 2 * x + 3 * y + z **2 - 4, x **2 + e** y + 4 * z - 15], [x, y, z])
    #     print(result)
    # except Exception as e:
    #     print('reason:{e},闫老师，您的数出错了，此题无解，请仔细出题！'.format(e=e))

    # x = sympy.Symbol('x')
    # f=5/(50+ln(x))
    #
    # a = sympy.integrate(f, (x, 1, 1.5))
    # print('闫老师，这个函数的原函数不是初等函数呢！积不出来，结果为：',a)

    # # 求微分方程
    # def fun1(x,f):
    #     return sy.diff(f(x),x,1)-f(x)**2-e**(x+5)
    # x = sy.Symbol('x',real = True) # real 保证全是实数，自变量
    # f=sy.Function('f',function = True) # 全部为函数变量

    # eq=(sy.Eq(f(x).diff(x,1)-f(x)**2-e**(x+5)), sy.Eq(f(x)-6))
    # sy.pprint(dsolve(eq))
    # sy.pprint(sy.dsolve(fun1(x,f),f(x)))

    # def f(x,y):
    #     return y**2+e**(x+10)
    # result=integrate.solve_ivp(f,(0,5),[5],dense_output=True)
    # print(result)

    # TUST_21820918
    X = 0
    Y = 9
    Z = 4
    N = 8
    # a、b、c、d、分别为
    a = 2 * X + Y - 2 * N
    b = 5 * N - 4 * Y + 2 * N
    c = 4 * X - 3 * N + 4 * Z
    d = 2 * X + Y - 5 * Z
    print(a, b, c, d)
    warnings.filterwarnings("ignore")
    # 1、求解如下方程组
    from scipy import optimize
    from math import e


    def f(x):
        x1, x2, x3 = x.tolist()
        return [a * x1 + b * x2 ** 2 + np.tanh(x3) - c,
                b * x1 - x2 + c * x3 ** 2 - d,
                x1 ** 2 + sin(x2) + 4 * x3 - 7]


    result = optimize.fsolve(f, [1, 1, 1])
    print(result)

    # 2 求解如下微分方程
    a = 0;
    b = 1;
    y0 = 20;
    n = 100
    h = (b - a) / n;
    u = [y0];
    L = []
    for i in range(n):
        L.append(a + i * h)
        K1 = h * (np.power(u[-1], 2) + np.exp(a * u[-1] + 2))
        K2 = h * (np.power((u[-1] + K1 / 2), 2) + np.exp((a * u[-1] + K1 / 2) + 2))
        u.append(u[-1] + 1 / 6 * (K1 + 2 * K2))
    L.append(b)
    print('第二题答案为：', L)
    print('************************')

    # 第三题
    from sympy import *
    X = 0
    Y = 9
    Z = 4
    N = 8
    def f(t):
        f = (Z + N) / (X + Y + Z + N + sin(t))
        return f
    x = symbols('x')
    truth = integrate(f(x), (x, 1, pi)).evalf()
    def t(n, a, b):
        h = (b - a) / n
        a += h
        tra_result = f(a)
        while (a + 2 * h) < b:
            a += 2 * h
            tra_result += f(a)
        return (2 * h * tra_result).evalf()
    a = 1;
    b = X + Y + Z;
    n0 = 0
    T0 = 0
    T = (1 / 2 * (b - a) * (f(a) + f(b))).evalf()
    while abs(T - T0) > 10 ** (-4):
        T0 = T
        n0 += 1
        n = 2 ** n0
        T = 1 / 2 * (T + t(n, a, b))
        print(T)
    print('第三题答案', truth)
    print('************************')

    # 4拉格朗日多项式
    from scipy.interpolate import lagrange
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [2, 4.6, 8 + X / 8, 4.6, 3 + (Y + Z) / 9.3, 2.2, 1 + (Z + N) / 20, -0.5]
    ret = lagrange(x, y)
    print(ret)
    for i in range(0, 100, 1):
        i = i / 10
        print(i, ' - ', ret(i))


    #5.线性回归
    import pandas as pd
    from numpy import mat
    from sklearn import linear_model
    data= pd.read_excel(r"data.xlsx",sheet_name='Sheet2')
    data=mat(data)
    x_zibian=data[:,[X-1,Y-1,Z-1]]
    y_yinbian=data[:,X+Y+N-1]
    try:
        regr = linear_model.LinearRegression()
        regr.fit(x_zibian,y_yinbian)
        print('coefficients(b1,b2):',regr.coef_)
        print('intercept(b0):',regr.intercept_)
    except:
        pass


    #6.动力学模型
    from scipy import optimize as op
    import numpy as np
    data_Ca= pd.read_excel(r"Ca.xlsx",sheet_name='Sheet1')
    t=data_Ca['时间(min)']
    t=np.array(t)
    Ca=data_Ca.iloc[:,N]
    Ca=np.array(Ca)
    Ca0 = np.array([Ca[0]])
    def func(Ca,betaa,k):
        return ((1/np.power(Ca, betaa-1))-(1/np.power(Ca0, betaa-1)))/(k*(betaa-1))
    def g(beta):
        return t - func(Ca,*beta)
    beta_start = (1.6,0.2)
    try:
        beta_opt,beta_cov = op.leastsq(g,beta_start)
        print(beta_opt)
        #Ca_cal=np.power(1/(beta_opt[0]*beta_opt[1]*t+(1/np.power(Ca0, beta_opt[0]-1))),1/(beta_opt[0]-1)
        import matplotlib.pyplot as plt
        import operator
        figsize = 11,9
        figure, ax = plt.subplots(figsize=figsize)
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.xlabel("时间/min")
        plt.ylabel("Ca")
        plt.scatter(t.tolist(), Ca.tolist(),s=15 ,c='r',marker='^') #实验值
        plt.scatter(t.tolist(), Ca.tolist(),s=15 ,c='b',marker='-') #计算值
        plt.legend()
    except:
        pass
