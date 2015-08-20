# -＊- coding: utf-8 -*-
from memory_profiler import profile

'''
Python 代码性能优化
优化通常包含两个方面： 减少代码的体积，提高代码的运行效率
Python性能分析模块
1. cProfile : 基于lsprof的用C语言实现的扩展应用，运行开销合理，适合分析运行时间长的程序。
2. profile : Python实现的性能分析模块，接口跟cProfile一样，可以自由扩展
3. hotshot :新版本被废弃

profile的最小粒度是“行”
1.CPU Profiler
   line_profiler
2.Memory Profiler
   memory profiler

'''
@profile
def fore_reserve(s):
    from collections import deque
    d =  deque()
    d.extendleft(s) #
    print d
    return ''.join(d)

if __name__ == "__main__":
    test_data = 'lqsh'
    print fore_reserve(test_data)

''' Result：
Line #    Mem usage    Increment   Line Contents
================================================
    19      7.2 MiB      0.0 MiB   @profile
    20                             def fore_reserve(s):
    21      7.2 MiB      0.0 MiB       from collections import deque
    22      7.2 MiB      0.0 MiB       d =  deque()
    23      7.2 MiB      0.0 MiB       d.extendleft(s) #
    24      7.2 MiB      0.0 MiB       print d
    25      7.2 MiB      0.0 MiB       return ''.join(d)
'''