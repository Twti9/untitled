#开发者：罗地观生
#开发时间：2021/4/27 20:49
try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入另外一个整数'))
    result = a // b
except ZeroDivisionError:#捕获异常并且按类型返回
    print('除数不能为0')
except ValueError:
    print('请输入整数')
except BaseException:#避免遗漏异常，最后可加上BaseException
    print('请正确输入整数')
else:
    print(result)


