"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/13 21:51
    @File : DNN.py
"""
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score

from Utils.GetAllDatas import GetDatas

if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()

    # 获取模型 None则设置基本模型为决策树
    dnn_regressor = BaggingRegressor(base_estimator=None,
                                     n_estimators=10, )
    # 训练
    dnn_regressor.fit(x_train, y_train)
    # 预测
    y_pred = dnn_regressor.predict(x_test)
    # 查看结果
    y1_score = r2_score(y_test, y_pred)
    print(y1_score)
