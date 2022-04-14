#开发者：罗地观生
#开发时间：2021/4/28 15:11
class Student:
    def __init__(self,name,age):
        self.name=name#self.name称为实例属性，将局部变量的name值赋给实例属性
        self.age=age
    def eat(self):
        print(stu1.name+'在吃饭')
stu1=Student('张安',50)
stu2=Student('李四',12)
print(id(stu1))
print(id(stu2))
'''为stu1动态绑定性别属性'''
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)
stu1.eat()
print('-------------为对象绑定方法---------------')
def show():
    print('来吧，展示！')
stu1.show=show
stu1.show()
print(stu1.name,stu1.age,stu1.gender)