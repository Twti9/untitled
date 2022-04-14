#开发者：罗地观生
#开发时间：2021/4/20 13:37
s='hello,python'
print('1.',s.isidentifier())#判断是否是合法的标识符
print('2.','abc'.isidentifier())
print('3.','acb_'.isidentifier())
print('4.','张三'.isidentifier())
print('5.','张三_123'.isidentifier())
print('6.','\t'.isspace())#判断指定的字符串是否是空白字符串组成的
print('7.','abc'.isalpha())#判断指定的字符串是否全部由字母组成
print('8.','12321'.isdecimal())#判断指定的字符串是否全部由十进制数字组成
print('9.','4564adbau'.isnumeric())#判断指定的字符串是否全部由数字组成
print('11.','ⅠⅡⅢⅣⅤ'.isnumeric())#罗马数字也是数字
print('10.','adgai456446'.isalnum())#判断指定字符串是否全部由字母和数字组成