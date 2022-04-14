#开发者：罗地观生
#开发时间：2021/4/20 12:57
s='python'
s1='PDYHhd,fdvdau,abduigd'
a=s.upper()#小写转大写
print(a,id(a))
print(s,id(s))
b=s1.lower()#大写转小写
print(b,id(b))
print(s1,id(s1))
c=s1.swapcase()#大小写相互转换
print(c,id(c))
d=s1.title()#每个字符串的首字母大写，其余均转为小写
print(d,id(d))
e=s1.capitalize()#将首个字符串的首字母大写，其余均为小写
print(e,id(e))