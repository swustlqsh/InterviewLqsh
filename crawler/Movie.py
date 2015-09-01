#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

import sys

import urllib
import urllib2

import re
import threading, Queue,time
from random import random

reload(sys)
sys.setdefaultencoding('utf-8') 

class MovThread(threading.Thread):
    movieQueue = Queue.Queue()
    threadTask = 10
    content = []
    def __init__(self):
        super(MovThread,self).__init__()
        self.header ={
               'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:32.0) Gecko/20100101 Firefox/33.0',
               'Connection':'keep-alive',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
                }

    def run(self):
        while not self.movieQueue.empty():
            url = self.movieQueue.get()
            page  = self.get_page(url)
            self.get_content(page)
            time.sleep(random() * 2)
            self.movieQueue.task_done()

    def get_page(self,url):
        req = urllib2.Request(url,urllib.urlencode({}),self.header)
        try:
            res = urllib2.urlopen(req)
            return res.read().decode('utf-8')
        except urllib2.URLError,e:
            return e.reason

    def get_content(self,page):
        if page == 'Not Found':
            return
        # pass

    def save_data(self):
        with open('/temp/movie.txt','w+') as fp:
            for name in self.content:
                fp.write(name + '\n')

    if __name__ == '__main__':
        # init
        MovThread.movieQueue.put(url) # add url
        threads = map(lambda th:MovThread(),xrange(MovThread.threadTask))
        map(lambda th:th.start(),threads) # make all the threads start their activates
        map(lambda th:th.join(),threads) # block until all threads are terminated
        MovThread.save_data() # save data
















