#开发者：罗地观生
#开发时间：2021/4/29 11:53
class Animal:
    def eat(self):
        print('动物会吃')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Person:
    def eat(self):
        print('人吃五谷杂粮')
def fun(obj):
    obj.eat()
fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())