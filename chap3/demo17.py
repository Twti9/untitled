#开发者：罗地观生
#开发时间：2021/4/18 18:48
'''元组是不可变序列，其内的对象也不允许改变'''
t=('python','made',[20,30,50],98)
print(type(t[0]))
print(type(t[1]))
print(type(t[2]))
t[2].append(15)
print(t[2])
#t[2]=100#不允许改变对象的引用，但是对象本身是列表，所以可以改变列表数据
print(t)
for  item in t:
    print(item)