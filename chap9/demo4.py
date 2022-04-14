#开发者：罗地观生
#开发时间：2021/5/3 14:37
src_file=open('log.jpg','rb')
target_file=open('copylog.jpg','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()