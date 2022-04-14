#开发者：罗地观生
#开发时间：2022/2/6 16:58
class treenode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
#初始化节点
n1=treenode(3)
n2=treenode(4)
n3=treenode(5)
n4=treenode(1)
n5=treenode(2)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5