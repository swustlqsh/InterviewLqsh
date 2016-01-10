# -*- coding:utf-8 -*-
from __future__ import print_function, division, unicode_literals

# 美化发送消息
class Beautify(float):
    def __repr__(self):
        return "%.6f" % self

def beautify_floats(obj):
    if isinstance(obj, float):
        return Beautify(obj)
    elif isinstance(obj, dict):
        return dict((k, beautify_floats(v)) for k, v in obj.items())
    elif isinstance(obj, (list, tuple)):
        return map(beautify_floats, obj) # 1和2功能上等价
        #return list(beautify_floats(item) for item in obj) # 2
    else:
        return obj

if __name__ == "__main__":
    list_0 = [1.2, 2.34]
    list_1 = [1.2, 2.34, [1.234, 34.66788]]
    print(beautify_floats(list_0))
    print(beautify_floats(list_1))