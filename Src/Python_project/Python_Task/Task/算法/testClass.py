# auth: code_king
# time: 2022/10/23 11:55
# file: testClass.py

class GrandFather():
    def __init__(self, name):
        self.name = name

class Father(GrandFather):
    def __init__(self, name, gender):
        super().__init__(name)
        self.gender = gender

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def testClass(self):
        print('这个是我的名字：', self.name)


pre_son = Father('ss','女')
pre_son.testClass()

son = Father('初始的名字','男')
son.testClass()
son.setName('son')
son.testClass()
