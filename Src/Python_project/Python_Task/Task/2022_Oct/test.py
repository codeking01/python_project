import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def f_fit(x, a, b):
    return ((a * b * x) * 0.039) / (a * x + b)


x = np.array([20.39006572,
              45.76005289,
              83.04353551,
              116.4185004,
              # 122.9110121,
              179.3753732,
              # 242.6918251,
              263.6189257,
              364.4625769,
              469.7348763,
              ])
y = np.array([3.370424637,
              8.282378792,
              15.21548491,
              18.5427632,
              # 22.53819327,
              23.6418222,
              # 31.09776469,
              32.80004017,
              31.59997011,
              32.87396481,
              ])
# p_fit是拟合系数 p_fit[0]是a p_fit[1]是b，如果参数多了依次类推,p0是他们的数量级差别
p_fit, pcov = curve_fit(f_fit, x, y,p0=np.array([1,100]))
print('p_fit',p_fit)
print('pcov',pcov)
print('Correlation coefficients:')
y_hat = f_fit(x, p_fit[0], p_fit[1])
print(np.corrcoef(y_hat, y))

# ax = plt.gca()
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))

plt.plot(x*0.01, y, 'o', label='Original Values')
# plt.plot(x, f(x), 'g', label='Original Curve')
plt.plot(x*0.01, y_hat, 'r', label='Fitting Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)
plt.title('scipy fitting')
plt.show()