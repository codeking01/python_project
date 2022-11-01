# auth: code_king
# time: 2022/10/25 11:28
# file: Testgetatter.py
class A(object):
    def r2(self, a, b):
        x = a
        a = b
        b = x
        print(a, b)


class B(object):
    def r2(self, a, b):
        try:
            x = a
            a = b
            b = x
            print(a/ b)
        except Exception as e:
            print(e)

    # B.r2(a=100,c=100)


d = B()
testR2 = getattr(d, 'r2')
testR2(a='5', b='2')
#  实例化
a = A()
c = getattr(a, 'r2')
a.r2(a='test1', b='test2')
c(a=5, b=0)
print('****')
b = A()
