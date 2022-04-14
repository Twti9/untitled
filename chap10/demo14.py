#开发者：罗地观生
#开发时间：2021/5/11 16:04
class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score
class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course=course
p=Person('Tim','Male')
s=Student('bob','male',88)
t=Teacher('adbahs','fbajf','afbafg')