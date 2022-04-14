#开发者：罗地观生
#开发时间：2021/4/20 17:35
'''函数定义和调用'''
def calc(a,b):#a,b称为形式参数，在函数定义处
    c=a+b
    return c
result=calc(10,20)#10,20为实参，为函数调用实际值，根据数据位置进行实参传递
print(result)
result=calc(b=10,a=20)#  =右边的b,a名称为关键字参数,按形参名称进行实参传递
print(result)
