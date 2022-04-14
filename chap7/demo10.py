#开发者：罗地观生
#开发时间：2021/5/2 14:50
class Cpu:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#(变量的赋值)
cpu1=Cpu()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
#类对象的浅拷贝
print('--------------------')
disk=Disk()#创建一个硬盘类对象
print(Disk,id(Disk))
computer=Computer(cpu1,disk)#创建一个计算机类的对象
#浅拷贝,对象包含的子对象内容不拷贝，源对象和拷贝对象使用同一个子对象
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
#深拷贝，对象包含的子对象也拷贝,源对象和拷贝对象所有子对象也不相同
print('**************')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)