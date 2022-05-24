# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put([42, None, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()
from multiprocessing import Pool, Process
from time import time, sleep
import pandas
import numpy as np

def test1():
    pass
def test2():
    pass
if __name__ == '__main__':
    t1=time()
    test1()
    test1()
    test1()
    test1()
    test1()
    test1()
    test1()
    test1()
    t2=time()

    t3=time()
    task1=Process(target=test2)
    task2=Process(target=test2)
    task3=Process(target=test2)
    task4=Process(target=test2)
    task5=Process(target=test2)
    task6=Process(target=test2)
    task7=Process(target=test2)
    task8=Process(target=test2)
    task1.start()
    task2.start()
    task3.start()
    task4.start()
    task5.start()
    task6.start()
    task7.start()
    task8.start()
    task1.join()
    task2.join()
    task3.join()
    task4.join()
    task5.join()
    task6.join()
    task7.join()
    task8.join()
    t4=time()
    print('正常的时间：',t2-t1)
    print('多进程的时间：',t4-t3)
    sleep(10)
#  0.49988269805908203

