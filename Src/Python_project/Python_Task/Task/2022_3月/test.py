# -*- coding: utf-8 -*-
# @Time : 2022/3/26 15:45
# @Author : code_king
# @File : test.py
import time
def display_time(func):
    def wrapper():
        t1 = time.time()
        result = func()
        t2 = time.time()
        print(t2 - t1)
        return result
    return wrapper


# 加一个装饰器 会跳转装饰器
@display_time
def plus_num():
    count = 0
    for i in range(2, 10000):
        if (i % 2 == 0):
            print(i)
            count += 1
    return count


if __name__ == '__main__':
    print(plus_num())
