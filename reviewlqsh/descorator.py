# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

# decorator
# no arguments decorator generate a new decorator function

def decorator_func_no_args(func):
    def handle_args(*args,**kwargs):
        print('begin')
        func(*args,**kwargs) #
        print('end')
    return handle_args




