#开发者：罗地观生
#开发时间：2021/5/11 13:21
'''指定顺序'''
template='hello{0},hello{1},hello{2},hello{3}.'
result=template.format('world','china','beijing','imooc')
print(result)
'''调整顺序'''
template='hello{3},hello{2},hello{1},hello{0}.'
result=template.format('world','china','beijing','imooc')
print(result)
#指定{}的名字w,c,b,i
template='Hello {w},Hello {c},Hello{b},Hello{i}.'
world='World'
china='China'
beijing='BeiJing'
imooc='imooc'
#指定名字对应的模板数据内容
result=template.format(w=world,c=china,b=beijing,i=imooc)
print(result)
T=(1,1,2,2,3,3,1,3,5,7,9)
print(T.count(1))
print(T.count(5))
print(T.index(9))
T=(1,'cH',[3,4])
L=T[2]
print(L)
L[1]=10
print(L)
print(T)
d={
    'Alice':45,
    'Bob':65,
    'Candy':84,
    'David':48
}
d['Alice']=72
d['David']=88
print(d)
d['Alice']=[72,96]
d['David']=[88,97]
print(d)
d['David'].append(41)
d['Alice'].append(58)
print(d)
'''for key in d:
    value=d[key]
    if value>60:
        print(key,value)'''
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
d.clear()
print(d)
s=set([1,4,3,2,5])
print(s)
names=['fhdasf','safasj','dhnasihdf']
new_names=['sgfj','safhi','sdhisaf']
name_set=set(names)
name_set.update(new_names)
print(name_set)
name_set.discard('sgfj')
print(name_set)