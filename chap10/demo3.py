#开发者：罗地观生
#开发时间：2021/5/8 8:10
'''列表生成式'''
print([char.upper()for char in 'abcde'])
print([(char.upper(),char) for char in 'abcde'])
print([2**i for i in range(1,11)if i%2==1])
nums=[1,2,3]
chars=['a','b','c']
print([c*n for n in nums for c in chars])
strings=['aa','bc','de']
print([char for string in strings for char in string])
'''字典生成式'''
print({char:char.upper() for char in 'abcde'})
'''集合生成式'''
print({char.upper()for char in 'abcde'})