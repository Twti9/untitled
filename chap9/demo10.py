#开发者：罗地观生
#开发时间：2021/5/3 15:43
import os
path=os.getcwd()
list_files=os.walk(path)#walk可以遍历指定位置下的所有目录和文件
for dirpath,dirname,filename in list_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('**************')
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print('--------------------------')