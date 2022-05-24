"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/6 21:33
    @File : 多线程之Pool.py
"""
import time
from multiprocessing import Process


def f():
    for i in range(33333333):
        k = i+i



def test2():
    for i in range(100000000):
        k = i+i


if __name__ == '__main__':
    t1 = time.time()
    worker1 = Process(target=f)
    worker2 = Process(target=f)
    worker3 = Process(target=f)
    worker1.start()
    worker2.start()
    worker3.start()
    worker3.join()
    t2 = time.time()

    t3 = time.time()
    test2()
    t4 = time.time()
    print('多进程时间：', t2 - t1)
    print('正常时间：', t4 - t3)
