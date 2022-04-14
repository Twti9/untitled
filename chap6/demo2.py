#开发者：罗地观生
#开发时间：2021/4/28 10:46
class Student:#类的创建
    native_pace='江西'#定义在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name=name#self.name称为实例属性，将局部变量的name值赋给实例属性
        self.age=age
    #实例方法
    def eat(self):#在类之内定义的叫方法，类之外定义的叫函数
        print('学生去食堂吃饭')
    #静态方法
    @staticmethod#静态方法用staticmethod修饰
    def sm():#用staticmethod修饰的类属性不允许使用self
        print('我使用了staticmethod方法修饰')
    #类方法
    @classmethod#类方法在类属性要加cls
    def cm(cls):
        print('hjdahgd')
#函数定义
def drink():
    print('学生去喝水')