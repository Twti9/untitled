#开发者：罗地观生
#开发时间：2021/4/19 14:05
s={10,20,30,40,51,'fie'}
print(s,type(s))
'''集合的添加元素方式1'''
s.add(13)#只增加一个元素
print(s)
s.update({15,14,19,61})#增加多个元素
print(s)
s.update(['sdh','dah',37,47])
print(s)
s.update(('sdfhu',398,'gfi'))
print(s)
#s.update(56)至少添加一个元素必须使用{},(),[]