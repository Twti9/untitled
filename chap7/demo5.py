#开发者：罗地观生
#开发时间：2021/4/29 10:38
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):#对object类的方法重写
        return '我的名字是{0},我今年{1}岁'.format(self.name,self.age)
stu=Student('中山',15)
print(dir(stu))
print(stu)#默认调用Student类中的str方法
print(type(stu))