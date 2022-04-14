#开发者：罗地观生
#开发时间：2021/5/11 17:21
import functools
int2=functools.partial(int,base=2)
print(int2('10000000'))
