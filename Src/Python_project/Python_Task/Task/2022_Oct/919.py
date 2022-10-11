import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize as op

x1 = np.array([
0.0634,
0.0701,
0.0768,
0.08,
0.0829,
0.0887,
0.0937,
0.0997,
0.1041,
0.1099,
0.1154,
0.1192,
0.1411,
0.1645,

])
x2 = np.array([
0.9366,
0.9299,
0.9232,
0.92,
0.9171,
0.9113,
0.9063,
0.9003,
0.8959,
0.8901,
0.8846,
0.8808,
0.8589,
0.8355,
])

T = np.array([
273.15,
283.15,
293.15,
298.15,
303.15,
313.15,
323.15,
333.15,
343.15,
353.15,
363.15,
373.15,
423.15,
473.15,
])
def f1(T,x1):
    Hm=25540
    Tm=1043.15
    y1=Hm/T*(1/Tm-1/T)-np.log(x1)
    return y1

def f2(x2,T,a12,a21,b12,b21):
    t12=a12+b12/T
    t21=a21+b21/T
    G12=np.exp(-0.3*t12)
    G21=np.exp(-0.3*t21)
    y2=x2**2*(t21*G21**2/(x1+G21*x2)**2+t12*G12/(x2+G12*x1)**2)
    return y2

def f3(beta):
    return f1(T,x1) - f2(x2,T,*beta)

beta_start = (-3.89,0.68,4284,-1830)
# beta_start = (1,1,1,1)
beta_opt= op.leastsq(f3,beta_start)[0]

print('a12:','%.2f'% beta_opt[0])
print('a21:','%.2f'% beta_opt[1])
print('b12:','%.2f'% beta_opt[2])
print('b21:','%.2f'% beta_opt[3])


def r2(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    r2=np.sum(np.multiply(x-x_mean,y-y_mean))**2/np.sum(np.power(x - x_mean,2))/np.sum(np.power(y - y_mean,2))
    return r2

y1=f1(T,x1)
y2=f2(x2,T,-0.54,-0.61,2551.05,836.73)
# y2=f2(x2,T,6.53,2.58,2131.84,165.89)
r2=r2(y1,y2)

my_font = {'family': 'Times New Roman',
           'weight': 'normal',
           'size': 50,
           }

plt.subplots(figsize=(15, 15), dpi=300)
plt.scatter(T, y1, label='left', color='orange', alpha=0.5, marker='*', s=100)  # s=50可以调整点的大小
plt.scatter(T, y2, label='right', color='blue', alpha=0.5, marker=11, s=100)
plt.xlabel('T (K)', fontproperties=my_font)
plt.ylabel('y', fontproperties=my_font)
plt.legend(loc='upper left', fontsize=20)
plt.grid(alpha=0.5, linestyle=':')
plt.savefig('./919_0.png')  # 保存图片
plt.close()