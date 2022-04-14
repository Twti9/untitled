#开发者：罗地观生
#开发时间：2021/4/20 13:10
s='hello,Python'
print(s.center(20,'*'))#设置居中对齐，设置字符宽度大于实际字符则平均分配填充
print(s.ljust(20,'*'))#设置左对齐，不足部分用*补足右边
print(s.ljust(10))#不设置参数则默认空格
print(s.rjust(20,'*'))#设置右对齐，不足部分补足左边
print(s.rjust(10))
'''右对齐，左边使用0填充'''
print(s.zfill(20))
print(s.zfill(10))
print('4568646'.zfill(20))
print('-4156484'.zfill(30))#-保持最左