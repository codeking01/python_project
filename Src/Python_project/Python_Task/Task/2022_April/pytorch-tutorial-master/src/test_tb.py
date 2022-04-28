"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/4/26 16:21
    @File : test_tb.py
"""
from torch.utils.tensorboard import SummaryWriter
writer=SummaryWriter("logs")
# y=x
for i in range(0,100):
    #
    writer.add_scalar("y=2x",2*i,i)

writer.close()