'''
@author king_xiong
@date 2022-7-17 20:38
'''
# 作者：星语者v
# 链接：https://www.zhihu.com/question/370155873/answer/1002737452
# 来源：知乎

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 自定义函数 e指数形式
def func(x, a, b):
    return ((a * b * x) * 0.039) / (a * x + b)


# 定义x、y散点坐标
x = [20.39006572,
     45.76005289,
     83.04353551,
     116.4185004,
     # 122.9110121,
     179.3753732,
     # 242.6918251,
     263.6189257,
     364.4625769,
     469.7348763,
     ]
x=np.array(x)
y=[3.370424637,
   8.282378792,
   15.21548491,
   18.5427632,
   # 22.53819327,
   23.6418222,
   # 31.09776469,
   32.80004017,
   31.59997011,
   32.87396481,
   ]
y=np.array(y)
# 非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
# 获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]
# c = popt[2]

yvals = func(x, a, b)
# 拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
# print('系数c:', c)

print('系数pcov:', pcov)
print('系数yvals:', yvals)
# 绘图
plot1 = plt.plot(x, y, 'black', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)
# 指定legend的位置右下角
plt.title('curve_fit')
plt.show()