#开发者：罗地观生
#开发时间：2021/5/3 16:27
import time
def showTime(fn):
    def getTime(*args):#*args获得fn的参数
        print('args is : ', args) #查看传入的参数
        print('calling time : ', time.time())
        if len(args) > 0:
            fn(args[0]) #要在修饰符函数中调用传入的函数参数fn，否则function1/function2是不会被调用的，仅仅只输出了时间信息
        else:
            fn()
    return getTime

@showTime
def function1(a):
    print('running function1 ')
    print('a = ', a)

@showTime
def function2():
    print('running function2 ')

function1(3)
function2()