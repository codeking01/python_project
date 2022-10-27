# auth: code_king
# time: 2022/10/20 19:44
# file: Test5.py

b=50

# todo 引用传递的解决
def test(**kwargs):
    print(kwargs)
    kwargs['h']['j']=80
    # print(kwargs['h']['j'])


if __name__ == '__main__':
    a={'j':50}
    test(h=a,d=50,z={'a':50})
