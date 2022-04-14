#开发者：罗地观生
#开发时间：2021/5/6 13:52
'''第一种方式输出前五的人名'''
name1='ldaiyu'
name2='jiabaoyu'
name3='xuebaocahi'
name4='wangfecahi'
name5='jiatanchun'
print('①\t'+name1)
print('②\t'+name2)
print('③\t'+name3)
print('④\t'+name4)
print('⑤\t'+name5)
'''第二种方式，使用列表'''
print('--------------------')
lst1=[name1,name2,name3,name4,name5]
lst2=['①','②','③','④','⑤']
for i in range(5):
    print(lst2[i],lst1[i])
'''使用字典键值对的方式'''
print('***************')
d={'①':name1,'②':name2,'③':name3,'④':name4,'⑤':name5}
for key in d:
    print(key+d[key])
'''使用zip函数'''
print('=====================')
for lst_sig,lst_name in zip(lst2,lst1):
    print(lst_sig,lst_name)


