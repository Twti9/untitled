#开发者：罗地观生
#开发时间：2022/2/6 17:07
dic={}
# 添加 key -> value 键值对
dic["小力"] = 10001
dic["小特"] = 10002
dic["小扣"] = 10003

# 从姓名查找学号
print(dic["小力"]) # -> 10001

names = [ "小力", "小特", "小扣" ]
def hash(id):
    index = (id - 1) % 10000
    return index
print(names[hash(10001)])