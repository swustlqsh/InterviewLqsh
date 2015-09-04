# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
# Keep it simple
# -------------------- one method --------------------
class SingkletonOne(object):
    def __new__(cls,*args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(SingkletonOne,cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(SingkletonOne):
    a = 1

# -------------------- two method --------------------
# Slight improvement
class SingletonTwo(object):
    def __new__(cls,*args,**kwargs):
        if not '_instance' in cls.__dict__:
            cls._instance =  object.__new__(cls)
        return cls._instance

class MClass(SingletonTwo):
    pass

# -------------------- three method --------------------
# decorator class
class SingletonThree:
    '''
     this is a class that implements the Singleton pattern
    '''
    def __init__(self,kclass):
        self.kclass = kclass
        self._instance = None

    def __call__(self,*args, **kwargs):
        if self._instance == None:
            self._instance = self.kclass(*args,**kwargs)
        return self._instance

@SingletonThree
class MyClass3():
    a = 1
    def __init__(self,x=0):
        self.x = x

# -------------------- fore method --------------------
# singleton function using decorator function
def singleton(cls,*args,**kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton


@singleton
class MyClass4(object):
    a = 1
    def __init__(self,x=0):
        self.x = x

# -------------------- five method --------------------
# __metaclass__ 使用元类的Python 高级用法
class Singletonfive(type):
    instance = None
    def __call__(cls,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super(Singletonfive,cls).__call__(*args,**kwargs)
        print('this is call function')
        return cls.instance

class Foo(object):
    a = 1
    __metaclass__ = Singletonfive



one = Foo()
two = Foo()
two.a = 3
print one.a # 3
# one is same with two. check it by id(), ==, is
# check it by id
print id(two) # 140675560691856
print id(one) # 140675560691856
# check it by ==
print one == two # True
# check it by is
print one is two # True
assert one is two



