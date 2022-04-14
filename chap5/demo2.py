#开发者：罗地观生
#开发时间：2021/4/25 14:39
def fun(arg1,arg2):
    print('agr1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)
n1=11
n2=[10,20,30]
print('**************')
print('n1=',n1)
print('n2=',n2)
print('-----------------')
fun(n1,n2)#位置传递，arg1和arg2是函数定义处的形式参数，n1，n2是函数调用处的实际参数
print('++++++++++++')
print('n1=',n1)
print('n2=',n2)
'''函数调用时，参数的的传递过程中函数体内
对不可变对象的修改不会影响实参的值，
对可变对象的修改会改变实参的值'''