#开发者：罗地观生
#开发时间：2021/4/17 11:11
for item in range (100,999):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if ge**3+shi**3+bai**3==item:
        print(item)