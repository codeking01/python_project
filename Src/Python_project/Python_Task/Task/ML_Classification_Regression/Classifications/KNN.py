"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/15 13:19
    @File : KNN.py
"""
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from Utils.GetAllDatas import GetDatas

if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()
    # 数据预处理 归一化 标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)
    # 获取模型
    Knn_classifier=KNeighborsClassifier()
    Knn_classifier.fit(x_train, y_train.astype(int).astype(float))
    # 预测
    y_pred=Knn_classifier.predict(x_test)
    y1_score=r2_score(y_test,y_pred)
    print(y1_score)