#开发者：罗地观生
#开发时间：2021/5/2 13:31
'''特殊方法的重写'''
a=100
b=20
c=a+b
d=a.__add__(b)
print(c)
print(d)
class A:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1='张三'
stu2='李四'
s=stu1+stu2
s1=stu1.__add__(stu2)
print(s1)
print(s)
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
print(stu1.__len__())
print(len(stu1))