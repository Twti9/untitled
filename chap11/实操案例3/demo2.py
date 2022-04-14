#开发者：罗地观生
#开发时间：2021/5/7 10:41
scores=(('广州恒大',70),('北京国安',77),('江西财大',76),('江西农大',79))
for index,item in enumerate(scores):
    print(index+1,'.',end='  ')
    for score in item:
        print(score,end='  ')
    print()