# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
# stacks

# method one
class Stack(list):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        try:
          return self.items.pop()
        except IndexError,e:
            print('index error')
            print(e)

    def peer(self):
        if self.isEmpty():
            print('stack is empty')
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

# method two
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class ListStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self,item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        if node:
             self.top = node.next
             return node.value
        else:
            raise Exception('stack is empty')


    def peer(self):
        try:
           return self.top.value
        except Exception,e:
            print(e)

    def size(self):
        node = self.top
        if node is None:
            return 0
        else:
            n = 1
        while node.next:
            n = n + 1
            node = node.next
        return n

if __name__ == '__main__':
    stack = ListStack()
    stack.push(1)
    print(stack.peer())
    stack.pop()
    print(stack.size())
