#开发者：罗地观生
#开发时间：2021/4/19 14:37
s={10,20,30,40,50}
s1={10,20,30,40}
s2={30,40,50}
'''集合的数学操作'''
'''交集'''
print(s.intersection(s1))
print(s & s1)#等价于intersection
'''并集'''
print(s1.union(s2))
print(s1|s2)
'''差集'''
print(s1.difference(s2))
print(s1-s2)
'''对称差集'''
print(s1.symmetric_difference(s2))
print(s1^s2)