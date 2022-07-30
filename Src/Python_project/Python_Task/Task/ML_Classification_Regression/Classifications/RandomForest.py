"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/15 13:30
    @File : RandomForest.py
"""
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

from Utils.GetAllDatas import GetDatas
"""
出结果很慢
"""

if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()
    # 数据预处理 归一化 标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)

    # 获取模型  随机森林
    Rfc=RandomForestClassifier()
    # 梯度提升树
    Gbc=GradientBoostingClassifier()
    # 训练模型
    Rfc.fit(x_train, y_train.astype(int).astype(float))
    Gbc.fit(x_train, y_train.astype(int).astype(float))
    # 测试数据
    y_1 = Rfc.predict(x_test)
    y_2 = Gbc.predict(x_test)

    # 预测结果，用的 r2_score
    #计算拟合的结果（测试集的）
    y1_score=r2_score(y_test,y_1)
    y2_score=r2_score(y_test,y_2)

    print(y1_score)
    print(y2_score)

