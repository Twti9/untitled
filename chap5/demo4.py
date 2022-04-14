#开发者：罗地观生
#开发时间：2021/4/27 19:17
def fun(*args):#函数定义时，可变的位置形参需要加*
    print(args)

fun(10)
fun(10,30,50)#将以元组形式输出多个数据
def fun1(**args):#函数定义时，可变的关键字形参需要加**
    print(args)

fun1(a=1,b=4)
fun1(a=10,b=23,c=36)#将以字典键值对形式输出数据
'''def fun2(*args,args):
    pass
    以上代码出错，同一时间只能定义一个位置形参'''
'''def fun2(**args,**args)
    pass
    以上代码出错，同一时间只能定义一个关键字形参
'''
#当可变位置参数和可变关键字参数在同一函数内定义时，可变位置形式参数要在可变关键字形式参数之前
def fun2(*args1,**args2):#参数名称不能一致
    pass