# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
from copy import deepcopy
from collections import deque

class group(object):
    def __init__(self):
        pass
    def __str__(self): # for user
        pass
    def __repr__(self): # for dev
        pass

# method one
class Fib:
    def __init__(self):
        self.array = [0,1]
    def getindex(self,n):
        assert isinstance(n,int)
        n = n-1
        if n == 0:
            return self.array[0]
        elif n == 1:
            return self.array
        else:
            for i in range(2,n+1):
                self.array.append(self.array[i-2] + self.array[i-1])
            return self.array
# test code
fib = Fib()
print fib.getindex(5)

# method two iter object
class FibInter(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def next(self):
        self.b, self.a =  self.a + self.b, self.b
        if self.b > 100:
            raise StopIteration();
        return self.a
    def __getitem__(self,n):
        assert isinstance(n,int) # assert
        a,b = 1,1
        for x in range(n):
            a,b = b, a + b
        return a
# test code
f = FibInter()
print f[0]
print f[1]
print f[2]
print f[3]



