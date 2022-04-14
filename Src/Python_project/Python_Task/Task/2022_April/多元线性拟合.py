# -- coding: utf-8 --
# @Time : 2022/4/14 11:15
# @Author : codeking
# @File : 多元线性拟合.py

import pandas
from sklearn import linear_model
# -javaagent:C:\\All_Softwares\\Develop_Tools\\JetBrains\\IntelliJ_IDEA_2021.3.3\\ja-netfilter\\ja-netfilter.jar
if __name__ == '__main__':
    df = pandas.read_csv('cars.csv')
    X = df[['Weight', 'Volume']]
    y = df['CO2']
    # 在 sklearn 模块中，我们将使用 LinearRegression() 方法创建一个线性回归对象。
    # 该对象有一个名为 fit() 的方法，该方法将独立值和从属值作为参数，并用描述这种关系的数据填充回归对象：
    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    # 现在，我们有了一个回归对象，可以根据汽车的重量和排量预测 CO2 值：
    # 预测重量为 2300kg、排量为 1300ccm 的汽车的二氧化碳排放量：
    predictedCO2 = regr.predict([[2300, 1300]])
    print(predictedCO2)