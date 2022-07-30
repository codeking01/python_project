"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/6 13:25
    @File : 多线程.py
"""
import threading

"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/4 16:40
    @File : test.py
"""
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
    threads=[]
    func1=Thread(target=test2)
    func2=Thread(target=test3)
    func3=Thread(target=test4)
    func1.start()
    func2.start()
    func3.start()

    """
     func1.setDaemon(True)#把当前线程设置为守护线程
     func2.setDaemon(True)#把当前线程设置为守护线程
     func3.setDaemon(True)#把当前线程设置为守护线程    
    """
    # 添加线程到线程列表
    threads.append(func1)
    threads.append(func2)
    threads.append(func3)
    # 等待所有线程完成
    for t in threads:
        t.join()
    func1.join()
    func2.join()
    func3.join()

def printtest2():
    # def test2():
    for i in range(10):
        time.sleep(1)
        print(i)

# func=Thread(target=test2)

if __name__ == '__main__':
    t1=time.time()
    printtest()
    t2=time.time()
    print('时间：',t2-t1)
    #  3.016688108444214

    t3=time.time()
    printtest2()
    t4=time.time()
    print('不开线程的时间：',t4-t3)
    #  10.093908309936523


    # 非独立线程的时候需要加锁操作数据
    # lock = threading.Lock()#生成全局锁
    # global num#在每个线程中都获取这个全局变量
    # print('---get num:',num)
    # time.sleep(1)
    # lock.acquire()#修改数据前加锁
    # num -= 1#对此公共变量进行-1操作
    # lock.release()#修改后释放