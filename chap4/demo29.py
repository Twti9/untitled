#开发者：罗地观生
#开发时间：2021/4/20 13:52
s='hello,python'
print(s.replace('python','java'))#使用字符串去替换原字符串
s1='hello,python,python,python'
print(s1.replace('python','java',2))#第三个参数代表替换次数
s2=['hello','python','world']
print('|'.join(s2))#使用特殊符号连接字符串
print(''.join(s2))#不使用符号
t=('python','hello','daudg')
print('|'.join(t))
print('*'.join('dhgiagd'))#默认字符串为待分割序列