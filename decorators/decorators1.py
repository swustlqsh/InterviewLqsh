# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
import random

# first things first
# before you can understand decorators, you must first understand.
# how functions work: functions return a value based on the given arguments
def foo(far):
    return far + 1

print(foo(2) == 3)
print(type(foo))

# first class object
'''
In python,functions are first-class objects. The means that functions can be
passed around, and used as arguments, just like any other values(e.g, string,int,float)
'''
def call_foo_with_args(foo,far):
    return foo(far)

print(call_foo_with_args(foo,2))
# pass
# nested functions
def parent():
    print('printing from the parent function')
    def first_child():
        return 'print the first_child function'
    def second_child():
        return 'print the second_child function'
    # call nested functions
    print(first_child()) # first_child
    print(second_child()) # second_child
# test parent function
parent()

'''
printing from the parent function
print the first_child function
print the second_child function
'''
# returning function
# nested functions
def parent():
    print('printing from the parent function')
    def first_child():
        return 'print the first_child function'
    def second_child():
        return 'print the second_child function'
    # call nested functions
    try:
        pass

    except AssertionError:
        pass
    print(first_child()) # first_child
    print(second_child()) # second_child

# test parent function calculate the program runtime
def benchmark(func):
    import time
    def wrapper(*args,**kwargs):
        start_t = time.clock()
        res = func(*args,**kwargs)
        print('{0} time'.format(time.clock()-start_t))
        return res
    return wrapper

@ benchmark
def random_tree(n):
    temp = [n for n in range(n)]
    for i in range(n+1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp

print(random_tree(100))


# class decorator
class myDecorator:
    def __init__(self,func):
        self.func = func
        self.call = 0
    def __call__(self,*args,**kwargs):
        print("it decortator call")
        self.call += 1
        print("call=%d" % (self.call))
        self.func(*args,**kwargs)

@myDecorator
def foo(x,y):
     print("x=%d,y=%d"%(x,y))

foo(1,3) # call = 1  first call function
foo(2,3) # call = 2  second call function



