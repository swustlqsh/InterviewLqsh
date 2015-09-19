__author__ = 'vis'

from functools import partial,wraps

# without wraps decorator
def without_wraps(func):

    def wrapper(*args,**kwargs):
        print("call decorator function")
        return func(*args,**kwargs)

    return wrapper

def with_wraps(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("call decorator function")
        return func(*args,**kwargs)

    return wrapper

@with_wraps
def add(a,b):
    '''
     return a add b
    :param a:
    :param b:
    :return:
    '''
    print("{0} + {1} = {2}".format(a,b,a+b))

f = add(1,2)
print(add.__name__)
print(add.__doc__)