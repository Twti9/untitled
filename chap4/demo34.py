#开发者：罗地观生
#开发时间：2021/4/20 16:48
s='举杯邀明月，对影成三人'
print(s.encode(encoding='GBK'))#编码，使用GBK格式类型
print(s.encode(encoding='UTF-8'))#编码，使用UTF-8格式类型
'''解码'''
byte=s.encode(encoding='GBK')#编码
print(byte.decode(encoding='GBK'))#解码，两种格+式要保持一致

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
