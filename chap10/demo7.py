#开发者：罗地观生
#开发时间：2021/5/10 10:51
'''生成器的使用'''
def power_of_two():
    for exponent in range(11):
        yield 2**exponent#yield的用法与return类似，但是会记录下函数内的状态，下次执行生成器函数将从上次退出位置继续执行
p=power_of_two()
print(next(p))
print(next(p))
print(next(p))
'''生成器表达式'''
letters=(item for item in 'abc')
print(letters)
print(next(letters))
print(next(letters))
print('******************')
nums=[2**i for i in range(1,11)]#列表生成式
print(nums)
lst=[char.upper() for char in ['a','b','c','d']]
print(lst)
lst1=[(char.upper(),char) for char in ['a','b','c','d']]
print(lst1)
print('------------')
lst2=[2**i for i in range(1,11) if i%2==1]
print(lst2)
num=[1,2,3]
chars=['a','b','c']
lst3=[c*n for n in num for c in chars]
print(lst3)
strings=['aa','bb','cc']
lst4=[char for string in strings for char in string]
print(lst4)
'''字典生成式'''
dict1={char:char.upper() for char in 'abcde'}
print(dict1)
'''集合生成式'''
print('/*/*/*/*//*/*/*/*/*/*')
die={char.lower() for char in 'ABCDE'}
print(die)