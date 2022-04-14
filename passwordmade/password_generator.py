#开发者：罗地观生
#开发时间：2021/5/5
import randomchar
def generate_password(length):
    if length<4:
        raise ValueError('密码长度至少为4位！')
    random_char=randomchar.RandomChar()
    password=random_char.uppercase()
    password+=random_char.lowercase()
    password+=random_char.digit()
    password+=random_char.special()
    count=5
    while count<=length:
        password+=random_char.anyone()
        count+=1
    return password

def main():
    while True:
        password_length=input('请输入密码长度(8-20位)：')
        password_length=int(password_length)
        if password_length < 8 or password_length > 20:
            print('密码长度不符合规定!!!')
            print('请输入8-20位！')
            main()
        password=generate_password(password_length)
        print('为您随机生成的密码为：',password)
if __name__ == '__main__':
    main()


