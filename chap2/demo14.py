#开发者：罗地观生
#开发时间：2021/4/18 17:48
items=['books','others','bulivs']
prices=[98,86,75]#以少的字典为压缩依据
d={ item.upper() : price  for item,price in zip(items,prices)  }#字典组合，upper大写字符串，zip()函数压缩函数
print(d)