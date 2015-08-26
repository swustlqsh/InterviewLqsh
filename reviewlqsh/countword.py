# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com
from copy import deepcopy
from collections import defaultdict
from operator import itemgetter, attrgetter, methodcaller

punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')

n_words = defaultdict(int)
def count(doc_line):
    assert isinstance(doc_line,(str,unicode))
    doc_line = doc_line.strip()
    if len(doc_line) == 0:
        return
    doc_list = doc_line.split()  #  cut word
    for i, w in enumerate(doc_list): # fast for big list
        join_w = ' '.join(w) # add space in the string.ascii_letters
        words = ''.join([w.lower() for w in join_w.split() if w not in punct])
        n_words[words] += 1 #
# open english doc
with open('data/english.txt') as fp:
    line = fp.readline()
    count(line)
    while line:
        line = fp.readline()
        count(line)
# sorted
n_words = dict(n_words)
d = sorted(n_words.iteritems(),key=lambda (k,v): v,reverse=True) # sort dict by count of word
print(d) # print sorted dict
# print top 10
for n in d[:10]:
    print n[0]
