#开发者：罗地观生
#开发时间：2021/4/29 12:30
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建类的对象
x=C('jack',15)#x是C类型的一个实例对象
print(x.__dict__)#属性对象的实例字典
print(C.__dict__)#类对象的实例字典
print(x.__class__)#<class '__main__.C'>输出对象所属的类
print(C.__bases__)#C类的父类类型的元素
print(C.__base__)#C类的父类类型的第一个元素
print(C.mro())#输出类的层次结构
print(A.__subclasses__())#查看A 的子类列表