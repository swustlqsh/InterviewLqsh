# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

#lcs algorithm
class LCS:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.lena = len(self.a)
        self.lenb = len(self.b)
        self.my_list = [[0]*(self.lena+1)] * (self.lenb+1)

    def lcsLen(self,i,j):
        if i>=self.lena or j >= self.lenb:
            return 0
        elif self.a[i] == self.b[j]:
            return 1 + self.lcsLen(i+1,j+1)
        else:
            return max(self.lcsLen(i+1,j),self.lcsLen(i,j+1))

    def lcschs(self,i,j):
        for i in range(1,self.lena+1):
            for j in range(1,self.lenb+1):
                if self.a[i-1] == self.b[j-1]:
                    self.my_list[i][j] = 1 + self.my_list[i-1][j-1]
                elif self.my_list[i][j-1] > self.my_list[i-1][j]:
                    self.my_list[i][j] = self.my_list[i][j-1]
                else:
                   self.my_list[i][j] = self.my_list[i-1][j]


if __name__ == '__main__':
    a = 'abcdef'
    b = 'zxdefy'
    lcs  = LCS(a,b)
    print(lcs.lcsLen(0,0))