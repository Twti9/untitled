#开发者：罗地观生
#开发时间：2021/4/20 16:09
'''字符串的切片操作'''
s='hello,python'
s4='!'
s1=s[1:5:1]#开始位置，结束位置，步长，若不设定，默认从0开始到结束，步长为1
print(s1)
s2=s[:5:]
print(s2)
s3=s[:6:]
print(s3)
new_str=s1+s2+s3+s4
print(new_str)
s6=s[:-6:-1]#从右往左切
print(s6)