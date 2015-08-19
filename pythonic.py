# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
'''
知识储备
'''
# first, data exchange between a and b
a,b =10,11
a,b = b,a

# 去掉list中重复的元素
old_list = [1,1,2,3,2]
new_list = list(set(old_list))

# 翻转一个字符串
old_s = 'abcd'
new_s = old_s[::-1] # 步长设置为-1

'''
字符串翻转 共有5种方法，其中方法1是最简单的一种是步长为-1，输出字符串。
其他方法有：
2.交换前后字符的位置（非递归地方式）
3.交换前后字符的位置(递归地方式)
4. 双端队列，使用extendleft函数

'''
# one function
def one_reverse(s):
    return s[::-1]
# two function
def two_reserve(s):
    s_list = list(s)
    s_len = len(s)
    for before, after in zip(range(s_len-1,0,-1),range(s_len//2)):
        s_list[before], s_list[after] = s_list[after], s_list[before]
    return ''.join(s_list)

# three function
# tool function for the two function
def three_reserve_todo(start,end,s):
    if start < end and start != end:
       s[start],s[end] = s[end],s[start] # if s is type str.TypeError: 'str' object does not support item assignment
       return three_reserve_todo(start+1,end-1,s)
    else:
        join_s = ''.join(s)
        print 'reverse string: {}'.format(join_s)
        return join_s

def three_reserve(s):
    print 'raw string: {}'.format(s)
    tmp_s = ' '.join(s).split()  # list(s) is also used
    new_s = three_reserve_todo(0,len(s)-1,tmp_s)
    # use new_s
    # pass
'''
Notice that extendleft() iterates over its input and performs the equicvalent of an appendleft() for
each item. The end result is the deque contains the input sequence in reverse order.
'''
def fore_reserve(s):
    from collections import deque
    d =  deque()
    d.extendleft(s) #
    print d
    return ''.join(d)

# test data
# pass






