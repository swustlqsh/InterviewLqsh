# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

#merge list algorithm
# 求解已序数列的交集

a = [[1,2,3,6],[2,3,6,89],[2,3,5,6],[2,3,4,5,6],[3,5,6,7]]
'''
left_list: 有序的list
right_list: 有序的list
merge: 返回两者的交集

'''

def merge(raw_list):
    len_d = len(raw_list)
    if len_d == 1:
        return raw_list[0]
    if len_d == 2:
        return  [i for i in raw_list[0] if i in raw_list[1]]

    left_list,right_list = raw_list[0:len(raw_list)/2],raw_list[len(raw_list)/2:]
    raw_list = []
    raw_list.append(merge(left_list))
    raw_list.append(merge(right_list))
    return merge(raw_list)

if __name__ == '__main__':
    # test merge
    print(merge(a))