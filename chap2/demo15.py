#开发者：罗地观生
#开发时间：2021/4/18 17:55
'''可变序列和不可变序列'''
'''可变序列:列表，字典'''
lst=[10,20,30]
print(id(lst))
lst.append(50)
print(id(lst))
'''不可变序列：字符串，元组'''
s='hello'
print(id(s))
s=s+'world'
print(id(s))


