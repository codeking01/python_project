"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/13 17:55
    @File : DecisionTree.py
"""
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor

from Utils.GetAllDatas import GetDatas

if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()

    # 获取模型
    # 建立两个模型 看不同的模型深度对训练集的拟合程度 最大深度设的小会限制模型队训练集的拟合
    regr_1 = DecisionTreeRegressor(max_depth=15)
    regr_2 = DecisionTreeRegressor(max_depth=25)

    # 训练模型
    regr_1.fit(x_train, y_train)
    regr_2.fit(x_train, y_train)
    # 测试数据
    y_1 = regr_1.predict(x_test)
    y_2 = regr_2.predict(x_test)

    # 预测结果，用的 r2_score
    #计算拟合的结果（测试集的）
    y1_score=r2_score(y_test,y_1)
    y2_score=r2_score(y_test,y_2)
    print(y1_score)
    print(y2_score)

