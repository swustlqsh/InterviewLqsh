# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

# python 中四个魔法函数 __len__,__getitem__,__delitem__,setitem__
class MyList:
    __list = []
    def __init__(self):
        self.i = 0
        self.n = 0
        print('construction')

    def __del__(self):
        print('del')

    def __setitem__(self,item,value):
        self.__list[item] = value

    def __getitem__(self,item):
        return self.__list[item]

    def __delitem__(self,item):
        if item in self.__list:
            self.__list.remove(item)
    def __len__(self):
        return len(self.__list)

    def add(self,value):
        self.__list.append(value)

    def display(self):
        for item in self.__list:
            print item

    def __iter__(self):
        return self

    def next(self):
        if self.i <  len(self):
           temp = self.__getitem__(self.i)
           self.i += 1
           return temp
        else:
            raise StopIteration()

mylist = MyList() # construction
print mylist
print len(mylist) # 0
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.display()
# show all the items in the mylist
'''
1
2
3
4
'''
mylist.__setitem__(0,10)
print mylist.__getitem__(0)
mylist.__delitem__(10)
print len(mylist)
print mylist[1]
# iter object
print('iter object')
for item in mylist:
    print item






