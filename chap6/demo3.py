#开发者：罗地观生
#开发时间：2021/4/28 10:46
class Student:#类的创建
    native_pace='江西'#定义在类里的变量，称为类属性,为类里的所有对象共享
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
        print('类方法的调用')
#函数定义
def drink():
    print('学生去喝水')
stu1=Student('张三',20)#创建Student类的对象
print('***********')
stu1.eat()#对象名.方法名
print('1111111111111111111')
print(id(stu1))
print(type(stu1))
print(stu1.age)
print(stu1.name)
print('--------------')
Student.eat(stu1)
print(Student)#类名.方法名(类的对象)（）内的对象与方法定义处的self一样
print('----------类方法的调用-----------')
stu2=Student('李赛',10)
stu3=Student('wnagwu',34)
#访问类属性
print(Student.native_pace)
#修改类属性
Student.native_pace='北京'
print(Student.native_pace)
#类方法的调用
Student.cm()
#静态方法的调用
Student.sm()