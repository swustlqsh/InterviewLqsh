# -*- coding: utf-8 -*-
__author__ = 'vis'
# email: qiushengli245@gmail.com

class Coder:
    def findCoder(self,A,n):
        from collections import defaultdict
        from operator import itemgetter
        import re
        pattern = re.compile(r'coder',re.I)
        coder_dict = defaultdict(int)
        for i in range(n):
            text = A[i]
            coder_dict[i] = len(re.findall(pattern,text))
        #
        items = sorted(coder_dict.iteritems(),key=itemgetter(1,0),reverse=True)
        return [A[a[0]] for a in items]


if __name__ == '__main__':
    coder = Coder()
    print(coder.findCoder(['Coder','coder coder'],2))
    text = 'Coder coder Coder1334 fdfd'
    print(text)
    text.find('coder')
