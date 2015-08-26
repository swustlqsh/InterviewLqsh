# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
n = 4 # 参与全排列的数
a = [0]*n
b = [0]*n
# Depth First Search (DFS)
# permutation
def permu(step):
    if step == 4: # 当前站在n+1个盒子面前，表示前n个盒子的牌已经放好
        print a[1:]
        return # 返回之前的调用，最近的调用permu函数的地方
    for i in range(1,4):
        if b[i] == 0:
            a[step] = i
            b[i] = 1
            permu(step+1)
            b[i] = 0 # 收回刚才放牌，以便下一步尝试
    return  #

# test code
permu(1)

