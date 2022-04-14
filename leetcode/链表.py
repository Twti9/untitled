#开发者：罗地观生
#开发时间：2022/2/6 16:44
class listnode:
    def __init__(self,x):
        self.val=x
        self.next=None
n1=listnode(4)
n2=listnode(5)
n3=listnode(1)
n1.next=n2
n2.next=n3
print(n1.val)
print(n1.next.val)
