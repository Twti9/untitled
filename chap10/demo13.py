#开发者：罗地观生
#开发时间：2021/5/11 15:35
s1=set([1,2,3,4,5])
s2=set([1,2,3,4,5,6,7,8,9])
print(s1.issubset(s2))#判断s1是否为s2的子集
print(s2.issuperset(s1))#判断s2是否为s1的超集
print(s1.isdisjoint(s2))#判断集合是否重合
def data_of_square(side):
    c=4*side
    s=side*side
    return c,s
c,s=data_of_square(16)
print('周长={}'.format(c))
print('面积={}'.format(s))
def my_abs(x):
    if not isinstance(x,int)or not isinstance(x,float):
        print('parm type error.')
        return None
    if x>=0:
        return x
    else:
        return -x
def average(*args):
    sum=0
    for item in args:
        sum+=item
    avg=sum/len(args)
    return avg
print(average(10,12,32,54,87))
def info(**kwargs):
    print('name:{},gender:{},age:{}'.format(kwargs.get('name'),kwargs.get('gender'),kwargs.get('age')))
info(name='cagf',gender='girl',age='12')