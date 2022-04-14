#开发者：罗地观生
#开发时间：2021/5/6 13:20
'''使用print输出到文件'''
fp=open('f:/text.txt','w')
print('奋斗成就更好的你！',file=fp)
fp.close()
'''第二种操作，使用with open'''
with open('f:/test1.txt','w')as file:
    file.write('一寸光阴一寸金')
