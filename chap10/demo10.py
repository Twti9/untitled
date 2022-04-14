#开发者：罗地观生
#开发时间：2021/5/10 11:46
'''装饰器的使用'''
import datetime
import functools
def time(format):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print(datetime.datetime.now().strftime(format))
            return func(*args,**kwargs)
        return wrapper
    return decorator
@time('%Y/%m/%d %H:%M:%S')
def say_hello():
    print('hello')
say_hello()
print(say_hello)
print(say_hello.__name__)