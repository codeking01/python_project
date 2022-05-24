"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/4/28 22:45
    @File : lesson1.py
"""
import torch
import time
if __name__ == '__main__':
    print(torch.__version__)
    print('gpu:',torch.cuda.is_available())
    # 生成矩阵
    a=torch.randn(10000,1000)
    b=torch.randn(1000,20000)
    t0=time.time()
    # 矩阵相乘
    c=torch.matmul(a,b)
    t1=time.time()
    # norm求范数的
    print(a.device,t1-t0,c.norm(2))

    device=torch.device('cuda')
    a=a.to(device)
    b=b.to(device)
    t0=time.time()
    # 矩阵相乘
    c=torch.matmul(a,b)
    t1=time.time()
    print(a.device,t1-t0,c.norm(2))

    t0=time.time()
    # 矩阵相乘
    c=torch.matmul(a,b)
    t1=time.time()
    print(a.device,t1-t0,c.norm(2))