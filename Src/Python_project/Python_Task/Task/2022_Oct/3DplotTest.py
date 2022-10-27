# auth: code_king
# time: 2022/10/12 12:29
# file: 3DplotTest.py
import numpy as np
from scipy.optimize import curve_fit


def r2(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    r2 = np.sum(np.multiply(x - x_mean, y - y_mean)) ** 2 / np.sum(np.power(x - x_mean, 2)) / np.sum(
        np.power(y - y_mean, 2))
    return r2


# CEX0是x([X:,0]),CEX是z(X[:,1]),k3是a,k-3是b,k2`是k2。E0
# y=((k2`*b*x)*E0)/(k2`+a*z+(b-a)*x)

k2 = 1197
E0 = 0.0496


def f_fit(X, a, b):
    return ((k2 * b * X[:, 1]) * E0) / (k2 + a * X[:, 0] + (b - a) * X[:, 1])


x = np.array([21.15830425,
              45.48035652,
              60.22977019,
              83.04285454,
              108.9096476,
              139.6265276,
              ])
z = np.array([19.17436572,
              40.66102201,
              54.21635885,
              76.68262453,
              100.6623237,
              130.877381,
              ])
X = np.c_[x, z]
y = np.array([1.98393853,
              4.819334507,
              6.013411342,
              6.360230012,
              8.247323918,
              8.749146564,
              ])
# p_fit是拟合系数 p_fit[0]是a p_fit[1]是b，如果参数多了依次类推,p0是他们的数量级差别
p_fit = curve_fit(f_fit, X, y, p0=(1, 100), maxfev=10000)[0]
print('\nCorrelation coefficients:')
print('p_fit', p_fit)
# print('pcov', pcov)
y_hat = f_fit(X, p_fit[0], p_fit[1])
print('y_hat', y_hat)
print('r2_score:', r2(y_hat, y))
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax3d = fig.add_subplot(projection='3d')  #创建3d坐标系
# from mpl_toolkits.mplot3d import Axes3D
# ax = Axes3D(fig)   #创建3d坐标系的第二种方法

x = np.array([21.15830425,
              45.48035652,
              60.22977019,
              83.04285454,
              108.9096476,
              139.6265276,
              ])
z = np.array([19.17436572,
              40.66102201,
              54.21635885,
              76.68262453,
              100.6623237,
              130.877381,
              ])
X = np.c_[x, z]
y = np.array([1.98393853,
              4.819334507,
              6.013411342,
              6.360230012,
              8.247323918,
              8.749146564,
              ])

ax3d.plot(x,z,y,c='red',linestyle='-')  #绘制3d螺旋线
ax3d.plot(x,z,y_hat)  #绘制3d螺旋线
plt.show()