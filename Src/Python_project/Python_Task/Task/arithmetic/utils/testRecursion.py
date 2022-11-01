# auth: code_king
# time: 2022/10/28 11:00
# file: testRecursion.py
# 函数必须第一个参数，这个参数的作用是你求取第几个数字的阶乘
def func(recursion=None):
    if recursion == 1:
        return 1
    else:
        # 因为n！= n * n-1 ...*1,那么5！= 5*4！
        return recursion * func(recursion-1)

if __name__ == '__main__':
    break_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]

    result = func(5)
    # 打印结果
    print(result)
