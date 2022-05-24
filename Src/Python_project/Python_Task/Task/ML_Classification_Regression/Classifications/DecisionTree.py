"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/14 21:59
    @File : DecisionTree.py
"""
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from Utils.GetAllDatas import GetDatas

if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()
    # 类别型特征向量化
    # vec=DictVectorizer()
    # x_train=vec.fit_transform(x_train)
    # x_test=vec.transform(x_test)

    #类别型的 需要特征向量化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)
    # 获取模型
    regr_1 = DecisionTreeClassifier(criterion="gini",max_depth=15)
    regr_2 = DecisionTreeClassifier(criterion="gini",max_depth=25)
    # 训练模型
    regr_1.fit(x_train, y_train.astype(int).astype(float))
    regr_2.fit(x_train, y_train.astype(int).astype(float))
    # 测试数据
    y_1 = regr_1.predict(x_test)
    y_2 = regr_2.predict(x_test)
    # 预测结果，用的 r2_score
    #计算拟合的结果（测试集的）
    y1_score=r2_score(y_test,y_1)
    y2_score=r2_score(y_test,y_2)
    print(y1_score)
    print(y2_score)