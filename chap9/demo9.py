#开发者：罗地观生
#开发时间：2021/5/3 15:34
import os
'''获取指定目录下的所有文件'''
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)