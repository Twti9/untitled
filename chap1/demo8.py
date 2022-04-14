#开发者：罗地观生
#开发时间：2021/4/17 15:14
lst=[10,20,30,40,50,30,90]
lst.remove(90)
lst.pop(4)
print(lst)
lst.pop()
print(lst)
#lst.remove(30)#删除指定元素，元素不存在返回valueerror，元素重复时只删除第一个
#lst.pop(1)#删除指定索引位置的元素，元素不存在indexerror
#lst.pop()#不指定索引，删除列表最后一个元素
print('删除列表至少一个元素，将产生一个新的列表对象')
lst4=lst[1:3]
print('原列表',lst)
print('新列表',lst4)
'''不产生新列表对象，而是删除原列表中的元素'''
lst[1:3]=[]
#lst.clear()#清楚列表中的元素

#del lst#删除列表对象
#print(lst)