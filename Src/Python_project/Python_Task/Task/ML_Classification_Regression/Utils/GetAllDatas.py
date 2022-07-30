"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/13 16:07
    @File : GetAllDatas.py
"""

# 直接调用写死的路径，获取训练集和测试集
import numpy as np

def GetDatas():
    x_train=np.load(r'../All_datas/x_train.npy')
    x_test=np.load(r'../All_datas/x_test.npy')
    y_train=np.load(r'../All_datas/y_train.npy')
    y_test=np.load(r'../All_datas/y_test.npy')
    return x_train,x_test,y_train,y_test

# readpath='../All_datas/x_test.npy'
# GetDatas(readpath)
# x_train,x_test,y_train,y_test=GetDatas()