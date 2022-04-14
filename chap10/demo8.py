#开发者：罗地观生
#开发时间：2021/5/10 11:46
'''装饰器的使用'''
import datetime
def time(func):
    def wrapper(*args,**kwargs):
        print('[',datetime.datetime.now(),']')
        return func(*args,**kwargs)
    return wrapper
@time
def say_hello():
    print('hello')
say_hello()