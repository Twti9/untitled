#开发者：罗地观生
#开发时间：2021/4/27 20:59
try:
    a = int(input('请输入一个整数'))
    b = int(input('请输入另外一个整数'))
    result = a / b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)