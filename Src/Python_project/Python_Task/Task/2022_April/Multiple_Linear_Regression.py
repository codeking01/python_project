import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

#通过read_csv来读取我们的目的数据集
adv_data = pd.read_csv("Advertising.txt", sep='	')

# #得到我们所需要的数据集且查看其前几列以及数据形状
print(adv_data.head(10))

# 数据描述
print(adv_data.describe())
# 缺失值检验
print(adv_data[adv_data.isnull() == True].count())

adv_data.boxplot()
plt.savefig("箱图.jpg")
plt.show()

adv_data.iloc[:, :3].hist(bins=30,alpha = 0.5)
plt.savefig("直方图.jpg")
plt.show()

adv_data.iloc[:, :3].plot(kind='kde', secondary_y=True)
plt.savefig("密度图.jpg")
plt.show()
