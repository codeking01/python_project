"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/13 16:04
    @File : RandomForest.py
"""
from sklearn.metrics import r2_score

from Utils.GetAllDatas import GetDatas
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor

if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()

    # 获取模型
    # 参数不要的话，可以全部删除
    regr_1 = RandomForestRegressor(n_estimators=100,
                                   criterion="squared_error",
                                   max_depth=15, )  # 最大深度为15
    # 极端随机森林
    regr_2 = ExtraTreesRegressor()
    # 梯度提升树模型
    regr_3 = GradientBoostingRegressor(loss="squared_error",
                                       learning_rate=0.1,
                                       n_estimators=100,
                                       subsample=1.0,
                                       criterion="friedman_mse",
                                       max_depth=15, )

    # 训练模型
    regr_1.fit(x_train, y_train)
    regr_2.fit(x_train, y_train)
    regr_3.fit(x_train, y_train)
    # 测试数据
    y_1 = regr_1.predict(x_test)
    y_2 = regr_2.predict(x_test)
    y_3 = regr_3.predict(x_test)

    # 预测结果，用的 r2_score
    #计算拟合的结果（测试集的）
    y1_score=r2_score(y_test,y_1)
    y2_score=r2_score(y_test,y_2)
    y3_score=r2_score(y_test,y_3)

    print(y1_score)
    print(y2_score)
    print(y3_score)

