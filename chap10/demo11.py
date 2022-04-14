#开发者：罗地观生
#开发时间：2021/5/11 12:29
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
li=[1,2,3,0]
print(all(li))
print(any(li))
print(sorted([2,4,7,1,8]))
print(sorted([2,4,7,3,9],reverse=True))
print(sorted(['a','b','C','D','d'],key=str.lower))#字符串无关大小写排序
a=[1,2,3,4]
print(a.reverse())
print(a)
for item in range(1,5):
    print(item,end='')
    pass
print('\n')
print(zip([1,2,3],['a','b','c']))
a=zip([1,2,3],['a','b','c'])
print(list(a))
print(list(zip([1,2,3],['a','b'])))
print('\n')
seasons=['spring','summer','fall','winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=5)))#从第五个主键开始索引
set1={'1','2'}
list1=['1','2','5','3']
set2=set(list1)
print(set1)
print(set2)
setA={'1','2'}
setA.add('3')
print(setA)
setA.clear()
print(setA)
a={32,12,34}
b={12,43,123}
print(a.difference(b))#a-b
print(a.intersection(b))#a&b
print(a.union(b))#a并b
#参数的移除和获取
a={12,13,14,15}
print(a.pop())
print(a)
a.discard(13)#移除指定元素
print(a)
a={1,2,3}
b={4,5,6}
a.update(b)
print(a)