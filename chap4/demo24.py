#开发者：罗地观生
#开发时间：2021/4/19 15:43

s='hello,hello'
print(s.find('lo'))#查找lo第一次出现的位置
print(s.index('lo'))
print(s.rindex('lo'))#查找lo最后一次出现的位置
print(s.rfind('lo'))

print(s.find('k'))#查找不存在的字符不报错，返回-1
#print(s.rindex('k'))#报错
print(s.rfind('c'))#不报错，返回-1
#print(s.index('c'))#报错