#开发者：罗地观生
#开发时间：2022/2/6 17:15
from heapq import heappush,heappop
#初始化小顶堆
heap=[]
#元素入堆
heappush(heap,1)
heappush(heap, 8)
heappush(heap, 2)
heappush(heap, 4)
heappush(heap, 6)
print(heap)
#元素出堆 从小到大
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
'''大顶堆小顶堆都是基于完全二叉树的数据结构，
大顶堆：任意节点的值不大于其父节点的值
小顶堆：任意节点的值不小于其父节点的值'''