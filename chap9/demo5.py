#开发者：罗地观生
#开发时间：2021/5/3 14:53
with open('log.jpg','rb') as src_file:
    with open('copylog2.jpg','wb') as target_file:
        target_file.write(src_file.read())