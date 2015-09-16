# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

# Implement a queue in Python
# 1
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception('Queue is empty')
        '''
        try:
            return self.items[-1]
        except IndexError,e:
            print('index error')
            print(e)
        '''
# 2





if __name__  == '__main__':
    q  = Queue()
    q.enqueue('li')
    q.enqueue('qiu')
    q.enqueue('sheng')
    print(q.size())
    print(q.dequeue())
    print(q.size())
    print(q.peek()) # get top item in queue


