# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
from random import shuffle
class Heap:

    def __init__(self,data_s=list()):
        self.items = data_s

    def heapLength(self):
        return len(self.items)-1

    def parent(self,index):
        return index / 2

    def left(self,index):
        return index * 2 + 1

    def right(self,index):
         return index * 2 + 2
    # heapify
    def __heapify(self,index,n):
        l = self.left(index)
        r = self.right(index)
        if l<=n and self.items[l] > self.items[index]:
            largest = l
        else:
            largest = index
        if r <= n and self.items[r] > self.items[largest]:
             largest = r
        if largest != index:
            self.items[index],self.items[largest] = self.items[largest],self.items[index]
            self.__heapify(largest,n)
        else:
            return

    def buildHeap(self):
        n = self.heapLength()
        for i in range(n/2,-1,-1): # [n/2, 0]
            self.__heapify(i,n)

    def heapSort(self): # use heap to build sorted array from the end
        self.buildHeap()
        n = self.heapLength()
        for i in range(n,0,-1):
            self.items[0],self.items[i] = self.items[i],self.items[0]
            n = n - 1
            self.__heapify(0,n)


if __name__ == '__main__':
    a = range(10)
    shuffle(a)
    print(a)
    heap = Heap(a)
    heap.heapSort()
    print(heap.items)





