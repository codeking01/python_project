from concurrent.futures import ThreadPoolExecutor
import threading
def action():
    for i in range (1000):
        print(threading.current_thread().name + '  ' + str(i))
# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=8)
# 向线程池提交一个task, 50会作为action()函数的参数
# 开启多线程
def Start_Thread (num):
    for i in range (8):
        k=pool.submit(action,num+i*1000,num+(i+1)*1000)
Start_Thread(10000)

pool.submit(action)
future1 = pool.submit(action)
# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action)
future3 = pool.submit(action)
future4 = pool.submit(action)
future5 = pool.submit(action)
future6 = pool.submit(action)
future7 = pool.submit(action)
future8 = pool.submit(action)