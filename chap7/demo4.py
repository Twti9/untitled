#开发者：罗地观生
#开发时间：2021/4/29 10:11
class Person(object):#父类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
class Student(Person):#继承了父类中的方法(Person)
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)#调用父类中的方法，但是保留父类的原来写法
        self.stu_no=stu_no
    def info(self):#对父类中的方法重写
        super().info()#对父类中的方法调用
        print('学号',self.stu_no)
class Teacher(Person):
    def __init__(self,name,age,teacher_year):
        super().__init__(name,age)
        self.teacher_year=teacher_year
    def info(self):#对父类中的方法重写
        super().info()#对父类中的方法调用
        print('教龄',self.teacher_year)
stu=Student('战三',15,'10001')
tea=Teacher('李四',51,20)
stu.info()
print('-------------------')
tea.info()