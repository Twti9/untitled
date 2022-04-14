#开发者：罗地观生
#开发时间：2022/2/6 16:52
#python中一般使用双端队列 collections.deque
from collections import deque
queue=deque()
queue.append(3)
queue.append(5)
queue.append(9)
queue.append(15)
queue.append(18)
print(queue.popleft())
x=queue.popleft()
print(x)
y=queue.pop()
print(y)
