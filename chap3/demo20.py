#开发者：罗地观生
#开发时间：2021/4/19 14:14
s=set({10,20,30,45,12,48,98})
print(s)
s.remove(10)#删除指定的元素，如果不存在会返回keyerror
print(s)
s.discard(30)#删除指定元素，元素不存在不报错
print(s)
s.pop()#随机删除一个元素，函数不能指定参数
print(s)
s.clear()#清空集合
print(s)