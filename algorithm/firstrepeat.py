# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

class FirstRepeat:

    def findFirstRepeat(self,A,n):
        from collections import defaultdict
        char_dict = defaultdict(int)
        for i in range(n):
            char_dict[A[i]] += 1
            if(char_dict[A[i]]>1):
                return A[i]

if __name__ == "__main__":
    binary = FirstRepeat()
    A = '111111122aa'
    print(binary.findFirstRepeat(A,len(A)))

