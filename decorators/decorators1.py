# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
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
