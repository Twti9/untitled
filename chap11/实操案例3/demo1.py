#开发者：罗地观生
#开发时间：2021/5/6 14:37
'''将10进制整数转为二进制'''
def fun():
    num=int(input('请输入一个整数：'))
    print(num,'的二进制数为',bin(num))
    print(str(num)+'的二进制数为 '+bin(num))
    print('%s的二进制数为 %s' % (num,bin(num)))
    print('{0}的二进制数为 {1}'.format(num,bin(num)))
    print(f'{num}的二进制数为:{bin(num)}')
    print('--------------')
    '''将十进制数转为八进制数'''
    print(num,'的八进制数为',oct(num))
    '''将十进制数转为十六进制数'''
    print(num,'的十六进制数为：',hex(num))
if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('输入错误，只能输入整数')
