"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/13 23:46
    @File : Support_Vector_Machines.py
"""
from sklearn.svm import SVR
from sklearn.metrics import r2_score

from Utils.GetAllDatas import GetDatas

if __name__ == "__main__":
    # 获取数据
    x_train, x_test, y_train, y_test = GetDatas()
    # 线性
    svr_linear = SVR(kernel='linear', degree=4, gamma="scale", C=1.0)
    # RBF  径向基核函数
    svr_rbf = SVR(kernel='rbf', degree=4, gamma="scale", C=1.0)
    # 多项式
    svr_poly = SVR(kernel='poly', degree=4, gamma="scale", C=1.0)
    # 训练模型
    svr_linear.fit(x_train, y_train.ravel())
    svr_rbf.fit(x_train, y_train.ravel())
    svr_poly.fit(x_train, y_train.ravel())
    y1=svr_linear.predict(x_test)
    y2=svr_rbf.predict(x_test)
    y3=svr_poly.predict(x_test)
    #计算拟合的结果
    y1_score = r2_score(y_test, y1)
    y2_score = r2_score(y_test, y2)
    y3_score = r2_score(y_test, y3)
    print(y1)
    print(y2)
    print(y3)