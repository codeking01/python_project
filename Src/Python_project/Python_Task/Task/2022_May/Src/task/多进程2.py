"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/6 13:36
    @File : 多进程.py
"""
"""多任务进程"""
import multiprocessing

import time
from threading import Thread


def printtest():
    def test2():
        for i in range(3):
            time.sleep(1)
            print(i)
    def test3():
        for i in range(3,3*2):
            time.sleep(1)
            print(i)
    def test4():
        for i in range(3*2,3*3):
            time.sleep(1)
            print(i)
    """进程"""
    p1 = multiprocessing.Process(target=test2)
    p2 = multiprocessing.Process(target=test3)
    p3 = multiprocessing.Process(target=test4)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

def printtest2():
    # def test2():
    for i in range(10):
        time.sleep(1)
        print(i)


def main():
    t1=time.time()
    printtest()
    t2=time.time()
    print('多进程的时间：',t2-t1)


if __name__ == '__main__':
    main()
