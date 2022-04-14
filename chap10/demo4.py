'''迭代器的使用'''
number=[1,2,3,4]
iterator=iter(number)
print(iterator)
print(next(iterator))
print(next(iterator))
print('__iter__' in dir(number))