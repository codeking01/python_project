'''
@author king_xiong
@date 2022-01-21 20:38
'''
# 作者：星语者v
# 链接：https://www.zhihu.com/question/370155873/answer/1002737452
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# 自定义函数 e指数形式
# def func(x, a, b):
#     return (a * 420 + b * np.log(420) - a * x - b * np.log(x)) / (0.039 * a * b)


# 定义x、y散点坐标
t = [9.06035,
     8.086175,
     9.205394444,
     9.6680875,
     8.545136667,
     7.505725,
     6.553288095,
     6.04741875,
     5.699075926,
     5.483901667,
     4.11787625,
     3.331261,
     3.0405175,
     2.068422778,
     1.62030875,
     1.319367,
     1.295705833
     ]
x = np.array(t)
num = [0.022256528,
       0.020415747,
       0.024359833,
       0.026877625,
       0.024216167,
       0.021510744,
       0.018858953,
       0.017622751,
       0.01685742,
       0.016527708,
       0.012415101,
       0.010076915,
       0.009471419,
       0.006489357,
       0.005166322,
       0.004235972,
       0.004488356
       ]

y = np.array(num)
# 非线性最小二乘法拟合
popt, pcov = curve_fit( x, y)
# 获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]

# yvals = func(x, a, b)
# 拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)

print('系数pcov:', pcov)
# print('系数yvals:', yvals)
# 绘图
plot1 = plt.plot(x, y, 'r', label='original values')
# plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)
# 指定legend的位置右下角
plt.title('curve_fit')
plt.show()
