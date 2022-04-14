#开发者：罗地观生
#开发时间：2021/5/10 10:43
'''自定义迭代器'''
class PowerOfTwo:
    def __init__(self):
        self.exponent=0
    def __next__(self):
        if self.exponent>10:
            raise StopIteration
        else:
            result=2**self.exponent
            self.exponent+=1
            return result
    def __iter__(self):
        return self
if __name__ == '__main__':
    p=PowerOfTwo()
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print('-------------------------------------')
    for item in p:
        print(item)
