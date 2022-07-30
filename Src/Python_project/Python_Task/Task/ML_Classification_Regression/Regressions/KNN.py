"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/13 20:56
    @File : KNN.py
"""

from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor

from Utils.GetAllDatas import GetDatas
"""
回归效果很差
"""
if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()

    # 获取模型
    # 平均回归
    uni_knr = KNeighborsRegressor(weights='uniform')
    # 根据距离加权回归
    dis_knr = KNeighborsRegressor(weights='distance')
    # 训练模型
    uni_knr.fit(x_train, y_train)
    dis_knr.fit(x_train, y_train)

    # 预测
    y_pred=uni_knr.predict(x_test)
    y_pred2=dis_knr.predict(x_test)
    y1_score=r2_score(y_test,y_pred)
    y2_score=r2_score(y_test,y_pred2)
    print(y1_score)
    print(y2_score)
