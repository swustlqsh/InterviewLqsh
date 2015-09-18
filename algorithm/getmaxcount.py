# -*- coding: utf-8 -*-
__author__ = 'vis'
# email: qiushengli245@gmail.com

#在给定字符串中找出出现次数超过半数以上的字符，将它输出
def getMaxCount(A,n):
    if n  != len(A):
        raise Exception('n is not equal to the length of A')
    val_pro = ''
    val_count = 0
    for item in A:
        if val_count == 0:
            val_count += 1
            val_pro = item
        elif val_count != 0 and val_pro == item:
            val_count += 1
        elif val_count != 0 and val_pro != item:
            val_count -= 1

    count  = 0
    half_count = n // 2
    for item in A:
        if val_pro == item:
            count += 1
            if count > half_count:
                break
    else:
        return "can't find item"
    return val_pro

if __name__ == "__main__":
    case_1 = 'abc' # can't find item
    case_2 = 'abccc' # return c
    print(getMaxCount(case_2,len(case_2)))
