#开发者：罗地观生
#开发时间：2021/4/20 16:19
'''字符串的格式化'''
name='张三'
age=32
'''first method'''
print('my name is %s,this year %d' % (name,age))#%为固定符号
'''second method'''
print('my name is {0},this year {1}'.format(name,age))#调用内置函数format
'''third method'''
print(f'my name is {name},this year {age}')#f-string