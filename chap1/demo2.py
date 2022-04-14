#开发者：罗地观生
#开发时间：2021/4/17 10:54
sum=0
a=1
while a<=100:
    if not bool(a%2):
        sum+=a
    a+=1
print('1到100之间的偶数和为',sum)