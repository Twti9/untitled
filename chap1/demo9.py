#开发者：罗地观生
#开发时间：2021/4/18 13:50
lst=[10,50,20,45,98,21]
print('排序前的原列表',lst)
lst.sort()
print('顺序排序后的列表',lst)
lst.sort(reverse=True)
print('降序排序之后的列表',lst)#reverse=True降序排序，reverse=False升序排序
new_lst=sorted(lst)
print('新产生的列表',new_lst)#升序排序
new_lst2=sorted(lst,reverse=True)#降序排序
print('降序排序的列表',new_lst2)
