# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
#
'''
for

else

'''
min = [1,0,0,1]
max = [255,255,255,255]

def test(num):
    global min,max
    if len(num) != 4:
        print('不是4位')
        return
    for i in range(4):
        if not str.isdigit(num[i]):
            print('不是数字字符')
            return
    else:
        print('全是数字字符')
    for i in range(4):
        n = int(num[i])
        if n < min[i] or n > max[i]:
            print('超出范围')
            return
    else:
        print('没有超出范围')
    print('OK')
# main test
if __name__ == '__main__':
    ip = '1.0.0.10'
    num = ip.split('.')
    test(num)
