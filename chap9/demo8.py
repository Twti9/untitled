#开发者：罗地观生
#开发时间：2021/5/3 15:18
import os.path
print('1',os.path.abspath('demo5.py'))#输出绝对路径
print('2',os.path.exists('demo3.py'),os.path.exists('demo10'))#判断文件是否存在
print('3',os.path.join('E:\\Python','demo4.py'))#将目录名与文件名拼接起来
print('4',os.path.split('F:\\untitled\\chap7\\demo13.py'))#将目录与文件名拆分
print('5',os.path.splitext('demo13.py'))#拆分文件与后缀名
print('6',os.path.basename('F:\\untitled\\chap7\\demo13.py'))#提取文件名
print('7',os.path.dirname('F:\\untitled\\chap7\\demo13.py'))#提取文件目录
print('8',os.path.isdir('F:\\untitled\\chap7\\demo13.py'))#判断是否为路径