#开发者：罗地观生
#开发时间：2021/4/28 15:46
'''封装性'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#年龄不希望在类的外部被使用，加两个_
    def show(self):
        print(self.name,self.__age)
stu=Student('站撒',15)
stu.show()
print(stu.name)
#print(dir(stu))
print(stu._Student__age)#在类的外部可以通过_类名__实例属性  访问