#开发者：罗地观生
#开发时间：2021/4/28 15:37
class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print('汽车已经启动')
car=Car('adfgafg')
car.start()
print(car.brand)
