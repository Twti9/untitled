#开发者：罗地观生
#开发时间：2021/4/27 16:59
def fun(num):
    odd=[]#存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
lst=[10,22,32,45,55,56]
print(fun(lst))
'''函数的要不要加return视情况而定
（1）如果函数不需要返回值，就不需要return
（2）如果函数返回值是一个，则返回的是类型
（3）如果返回值是多个，则返回的是元组'''
print('*****************************')
def fun1():
    print('hello')
fun1()

def fun2():
    return 'hello world'
res=fun2()
print(res)

def fun3():
    return 'hello','word'
print(fun3())