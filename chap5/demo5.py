#开发者：罗地观生
#开发时间：2021/4/27 19:33
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

lst=[10,20,30]
fun(*lst)#加上*将列表上的每个元素都转为位置实参传入
dic={'a':15,'b':54,'c':58}
fun(**dic)#加上**将字典上的每个元素都转为关键字实参传入
def fun4(a,b,*,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
#fun4函数调用
fun4(10,20,c=54,d=65)#*之后的参数必须使用关键字实参传递
fun4(a=10,b=20,c=12,d=31)
#函数定义时的形参顺序问题
def fun5(a,b,*,c,d,**args):
    pass

def fun6(*args,**args2):
    pass
def fun7(a,b=10,*args,**args2):
    pass
#函数内的局部变量前使用global则直接变为全局变量