#开发者：罗地观生
#开发时间：2021/4/18 14:26
#使用[]获取值
scores={'张三':45,'李四':74,'王五':30}
print(scores['张三'])
#print(scores['柽柳'])#值不存在报错，返回keyerror
'''第二种，使用get函数获取值'''
print(scores.get('李四'))
print(scores.get('陈六'))#返回none
print(scores.get('马琪',92))#92是查找马琪对应的value值不存在时返回的默认值