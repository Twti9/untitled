#开发者：罗地观生
#开发时间：2021/5/3 15:05
import os
print(os.getcwd())#输出当前操作目录
print(os.listdir('../chap9'))#返回指定路径下的文件和目录信息
#os.mkdir('newdir2')#创建新目录
#os.makedirs('A/B/C')#创建多级目录
#os.rmdir('newdir2')#删除目录
#os.removedirs('A/B/C')#删除多级目录
#os.chdir('F:\\untitled\\chap9')#设置path为当前工作目录
print(os.getcwd())