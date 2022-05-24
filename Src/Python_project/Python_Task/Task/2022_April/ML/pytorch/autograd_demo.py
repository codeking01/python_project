"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/4/28 23:11
    @File : autograd_demo.py
"""
import torch
from torch import autograd
if __name__ == '__main__':
    x=torch.tensor(1.)
    # 分别设置初值， requires_grad=True 代表求导
    a=torch.tensor(1.,requires_grad=True)
    b=torch.tensor(2.,requires_grad=True)
    c=torch.tensor(3.,requires_grad=True)

    # 计算函数
    y=a**2*x+b*x+c
    print('before: ',a.grad,b.grad,c.grad)
    # 关于y对a,b,c分别求偏微分
    grads=autograd.grad(y,[a,b,c])
    print('after: ',grads[0],grads[1],grads[2])
