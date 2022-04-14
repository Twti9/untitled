#开发者：罗地观生
#开发时间：2021/4/19 14:22
'''判断集合中是否有指定元素'''
s=set({10,20,30,40,50})
print(10 in s)
print(20 not in s)
'''判断两个集合是否相等'''
s1={10,30,40,50,20}#和元素顺序无关
s2={10,20,30}
s3={10,20,60}
print(s ==s1)
print(s2!=s3)
'''判断一个集合是否是另外一个集合的子集'''
print('-----1-----')
print(s2.issubset(s1))
print(s3.issubset(s1))
'''判断一个集合是否是另外一个集合的超集'''
print('-----2-----')
print(s1.issuperset(s2))
print(s2.issuperset(s3))
'''判断两个集合是否有交集'''
print(s1.isdisjoint(s2))#有交集返回False
print(s2.isdisjoint(s3))