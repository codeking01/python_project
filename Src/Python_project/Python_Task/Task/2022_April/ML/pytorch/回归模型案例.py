"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/4/28 23:57
    @File : 回归模型案例.py
"""

# 计算损失函数
# 迭代
from torch import nn

class LinearRegressionModel:
    def __init__(self,input_dim,out_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear=nn.Linear(input_dim,out_dim)
    def forward(self,x):
        out=self.linear(x)
        return  out

if __name__ == "__main__":
    input_dim =1
    out_dim =1
    model=LinearRegressionModel(input_dim,out_dim)