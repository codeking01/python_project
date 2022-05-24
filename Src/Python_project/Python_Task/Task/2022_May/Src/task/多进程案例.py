"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/6 21:12
    @File : 多进程案例.py
"""
# 多线程
# 最后完成的线程的耗时
# [TIME MEASURE] execute function: gene_1000_field took 3840.604ms
# 多进程
# [TIME MEASURE] execute function: gene_1000_field took 1094.776ms
# 执行时间和单个线程的执行时间差不多，目的达到
import math
import time
from multiprocessing import Process


def time_measure(func):
    def wrapper(*args):
        t1=time.time()
        func(*args)
        t2 = time.time()
        print('正常的时间：',t2-t1)
    return  wrapper

@time_measure
def test():
    for i in range(100000000):
        k=i*i

def test2():
    for i in range(33333333):
        k=i*i

if __name__ == '__main__':
    t1=time.time()
    worker1=Process(target=test2)
    worker2=Process(target=test2)
    worker3=Process(target=test2)
    worker1.start()
    worker2.start()
    worker3.start()
    # worker1.join()
    # worker2.join()
    worker3.join()
    t2=time.time()
    print('多进程的时间：',t2-t1)
    test()