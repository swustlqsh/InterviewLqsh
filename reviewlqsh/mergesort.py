# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
from copy import deepcopy
from collections import deque,defaultdict
from operator import itemgetter, attrgetter, methodcaller

# 二路归并排序
raw_list = [1,2,0,3,10,6]
'''
left 是有序的
right 是有序的
merge 函数将两个有序的集合整合一个有序的集合
'''
def merge(left,right):
    l_len = len(left)
    r_len = len(right)
    result = []
    i = 0
    j = 0
    while i< l_len and j< r_len:
        while i<l_len and left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        while i<l_len and j< r_len and left[i]>= right[j]:
            result.append(right[j])
            j = j + 1
    if i<l_len:
          result.extend(left[i:])
    if j<r_len:
          result.extend(right[j:])
    return result

def mergeSort(raw_data):
    length = len(raw_data)
    if length == 1:
        return raw_data
    left_list,right_list = raw_data[0:length/2],raw_data[length/2:]
    raw_data = merge(mergeSort(left_list),mergeSort(right_list))
    return raw_data
# test code
print mergeSort(raw_list)

