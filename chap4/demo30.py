#开发者：罗地观生
#开发时间：2021/4/20 14:10
'''字符串比较'''
a=b='python'
c='python'
d='apple'
print(c>d)#比较的是字符串中字符的原始数值大小，可以用ord查看
print(ord('c'),ord('a'))
s1='appleall'
s2='appl'
print(s1>s2)
print(ord('罗'))
print(chr(32599))
print(a==b)
'''is 比较的是id值是否相等'''
print(a is b )#is比较的是地址，==比较的是值和类型
print(id(a),id(b))