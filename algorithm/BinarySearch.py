# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

class BinarySearch:
    def findFirst(self,A,index,val):
        i = index
        while i >= 0 and A[i] == val:
            i = i -1

        return i + 1 # return the value of item is equal val


    def getPos(self,A,n,val):
        mi,ma = 0,n

        while mi <= ma:
            mid = (mi + ma) // 2
            if A[mid] == val:
                return self.findFirst(A,mid,val)
            elif A[mid]> val:
                ma = mid -1
            else:
                mi = mid +1

        return -1

if __name__ == "__main__":
    binary = BinarySearch()
    A = [1,2,2,3,3,3,3,4]
    print(binary.getPos(A,len(A),3))

