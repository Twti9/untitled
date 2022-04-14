#开发者：罗地观生
#开发时间：2021/5/11 16:20
'''class Student(object):
    __slots__ = ('name','gender','score')#限制添加属性
    def __init__(self,name,gender,score):
        self.name=name
        self.gender=gender
        self.score=score'''
from functools import reduce
lst=list([1,2,3,4,5,6,7,8,9])
def f(x):
    return x*x
for item in map(f,[1,2,3,4,5,6,7,8,9]):
    print(item)
print('''-------------------------------''')
def f1(x,y):
    return x+y
print(reduce(f1,[1,3,5,7,9]))#对list中所有元素求和
s='    123'
print(s.strip())#strip默认输出空白字符，包括'\n','\r','\t',''
'''filter(f,list)高阶函数,函数f的作用是对每个元素进行判断，返回TRUE或者FALSE'''
def is_odd(x):
    return x%2==1
for item in filter(is_odd,[1,4,6,7,9,12,17]):#过滤偶数
    print(item)
'''匿名函数lambda定义'''
result=[item for item in map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])]
print(result)