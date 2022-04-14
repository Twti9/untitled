#开发者：罗地观生
#开发时间：2021/4/20 13:22
'''从左边开始分割'''
s='hello world python'
lst=s.split()#不指定分隔符，默认空格
print(lst)
s1='welcome|to|bei|jing'
lst1=s1.split(sep='|')#按分隔符劈分
print(lst1)
lst1=s1.split(sep='|',maxsplit=2)#指定最大劈分次数，余下作为一个整体
print(lst1)
'''从右边开始分割'''
print(s1.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|',maxsplit=1))