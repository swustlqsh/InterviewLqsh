# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

from stacks import Stack
#  绝对路径转化为相对路径， for example. input: /home/news/../temp/game/../;
#  output: /home/tmp/

# method one
import os
def abs_to_relative_one(filepath):
    return os.path.abspath(filepath)
# method two
def abs_to_relative_two(s):
    stack = Stack()
    index = 0
    len_f = len(s)
    while index < len_f:
        while index< len_f and s[index] != '.':
            stack.push(s[index])
            index += 1
        point_count = 0
        while index<len_f and s[index] == '.':
            index += 1
            point_count += 1
        if point_count == 2:
            stack.pop()
            while not stack.isEmpty() and stack.peer() != '/':
                stack.pop()

        index += 1
    return ''.join(stack.items) # print relative path


if __name__ == '__main__':
    filepath = '/home/news/../temp/game/./../'
    print(abs_to_relative_one(filepath)+'/')
    print(abs_to_relative_two(filepath))

