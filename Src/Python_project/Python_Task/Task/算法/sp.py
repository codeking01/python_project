import numpy as np


class StatisticParameter(object):
    init_params = 100

    def __init__(self, x, y, I, init_params):
        self.x = x
        self.y = y
        self.I = I
        self.init_params = init_params

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_I(self):
        return self.I

    def get_init_params(self):
        return self.init_params

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_I(self, I):
        self.I = I

    def set_init_params(self, init_params):
        self.init_params = init_params

    # 我这是举了个例子介绍，可以不这样写。 这个代表静态方法 cls()方法来实例化一个对象，可以不用在下面方法传参。
    @classmethod
    def cls_applications(cls):
        print(cls.init_params)

    def r2(self):
        '''
        :return: 返回预测结果r方
        '''
        x_mean = np.mean(self.x)
        y_mean = np.mean(self.y)
        r2 = self.I * np.sum(np.multiply(self.x - x_mean, self.y - y_mean)) ** 2 / np.sum(
            np.power(self.x - x_mean, 2)) / np.sum(
            np.power(self.y - y_mean, 2))
        return r2

    def aae(self):
        aae = self.I * np.mean(np.abs(self.x - self.y))
        return aae

    def rmse(self):
        rmse = self.I * np.sqrt(np.mean(np.multiply(self.x - self.y, self.x - self.y)))
        return rmse

    def aad(self):
        aad = self.I * np.mean(np.abs((self.x - self.y) / self.y))
        return aad


if __name__ == '__main__':
    # 这个是测试那个静态方法展示了这个
    son = StatisticParameter(x=np.array([10, 20, 30, 40]), y=np.array([10, 20, 30, 40]), I=10, init_params=None)
    son.cls_applications()
    son_sec = StatisticParameter(x=np.array([10, 28, 30, 40]), y=np.array([10, 20, 30, 40]), I=50, init_params=None)
    R2 = son_sec.r2()
    print(R2)
    aae = son_sec.aae()
    print('aae:', aae)
    son_sec.set_I(500)
    # 查看修改后的I
    print('修改后的I', son_sec.get_I())
    rmse = son_sec.rmse()
    print('rmse:', rmse)
    son_sec.set_x(np.array([10, 28, 30, 80]))
    add = son_sec.aad()
    print('add:', add)
    print(son_sec.get_x())
