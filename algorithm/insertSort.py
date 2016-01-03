# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
from random import shuffle
# insert sort

def insertSort(s):
    for i in range(1,len(s)):
        key = s[i]
        j = i - 1
        while(j>=0) and (s[j]> key):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] =  key

s = range(10)
shuffle(s) # shuffle
insertSort(s) # insertSort
print('insertSort function generate ')
print(s)