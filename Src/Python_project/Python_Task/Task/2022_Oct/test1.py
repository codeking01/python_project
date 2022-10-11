import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def r2(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    r2 = np.sum(np.multiply(x - x_mean, y - y_mean)) ** 2 / np.sum(np.power(x - x_mean, 2)) / np.sum(
        np.power(y - y_mean, 2))
    return r2


def f_fit(X, a, b):
    return ((100 * b * X[:, 1]) * 0.05) / (100 + a * X[:, 0] + (b - a) * X[:, 1])


x = np.array([20.49462888,
              60.22977019,
              83.04285454,
              108.9096476,
              139.6265276,
              ])
z = np.array([19.55595904,
              55.03897975,
              76.68262453,
              100.6623237,
              130.877381,
              ])
X = np.c_[x, z]
y = np.array([0.938669842,
              5.190790447,
              6.360230012,
              8.247323918,
              8.749146564,
              ])
# p_fit是拟合系数 p_fit[0]是a p_fit[1]是b，如果参数多了依次类推,p0是他们的数量级差别
p_fit, pcov = curve_fit(f_fit, X, y, p0=(1, 100), maxfev=10000)
print('Correlation coefficients:')
print('p_fit', p_fit)
# print('pcov', pcov)
y_hat = f_fit(X, p_fit[0], p_fit[1])
print('y_hat', y_hat)
print('r2_score:', r2(y_hat, y))
# print(np.corrcoef(y_hat, y))

# ax = plt.gca()
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))

# plt.plot(X, y, 'g', label='Original Values')
# # plt.plot(x, f(x), 'g', label='Original Curve')
# plt.plot(X, y_hat, 'r', label='Fitting Curve')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=4)
# plt.title('scipy fitting')
# plt.show()

"""
三维线框图
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# 给y升级一个维度
y = y[np.newaxis, :]
y_hat = y_hat[np.newaxis, :]

flg = plt.figure('Wireframe', facecolor='lightgray')
# flg1 = plt.figure('Wireframe', facecolor='lightgray')
# ax3d1 = flg1.add_subplot(projection='3d')
# ax3d = mp.gca(projection='3d')
ax3d = flg.add_subplot(projection='3d')
ax3d.set_xlabel('CEX0', fontsize=14)
ax3d.set_ylabel('CEX', fontsize=14)
ax3d.set_zlabel('Y', fontsize=14)
# ax3d.plot_wireframe(X[:, 0], X[:, 1], y, rstride=10,
#                     cstride=10, color='dodgerblue')
# ax3d.plot_wireframe(X[:, 0], X[:, 1], y_hat, rstride=10,
#                     cstride=10, color='red',label='dodgerblue')
ax3d.scatter(X[:, 0], X[:, 1], y_hat, color='dodgerblue',label='dodgerblue')
ax3d.scatter(X[:, 0], X[:, 1], y, color='red',label='dodgerblue')
# ax3d.scatter(x,y,8,zdir='Y',c='black')
plt.show()
# plt.savefig('pic.jpg')
