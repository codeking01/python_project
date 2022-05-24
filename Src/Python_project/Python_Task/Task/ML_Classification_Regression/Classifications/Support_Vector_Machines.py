"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/15 13:35
    @File : Support_Vector_Machines.py
"""
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR, LinearSVC, SVC
from sklearn.metrics import r2_score

from Utils.GetAllDatas import GetDatas

"""
出结果很慢
"""
if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()

    # b数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 获取模型 核函数分别为 线性、径向基核函数、多项式
    reg_1 = SVC(C=1, kernel='linear', degree=4)
    reg_2 = SVC(C=1, kernel='rbf', degree=4)
    reg_3 = SVC(C=1, kernel='poly', degree=4)

    # 训练模型
    reg_1.fit(x_train, y_train.astype(int).astype(float))
    reg_2.fit(x_train, y_train.astype(int).astype(float))
    reg_3.fit(x_train, y_train.astype(int).astype(float))
    y1 = reg_1.predict(x_test)
    y2 = reg_2.predict(x_test)
    y3 = reg_2.predict(x_test)
    # 计算拟合的结果
    y1_score = r2_score(y_test, y1)
    y2_score = r2_score(y_test, y2)
    y3_score = r2_score(y_test, y2)
    print(y1)
    print(y2)
    print(y3)
