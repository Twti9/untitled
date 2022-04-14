#开发者：罗地观生
#开发时间：2021/5/3 16:35
#coding:utf-8
import time
def sayHello(fn):
    def hello(*args):
        print('Hello')
        fn(*args) # 2
    return hello # 1

def showTime(fn):
    def getTime(*args):#4  *args获得fn的参数
        print('args is : ', args) #查看传入的参数
        print('calling time : ', time.time())
        if len(args) > 0:
            n = args[0]
            n *= 2
            fn(n) #5  要在修饰符函数中调用传入的函数参数fn，否则function1/function2是不会被调用的，仅仅只输出了时间信息
        else:
            fn()
    return getTime # 3
@sayHello
@showTime
def function1(a): # 5
    print('running function1 ')
    print('a = ', a)
function1(3)