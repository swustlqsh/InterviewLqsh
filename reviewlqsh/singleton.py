# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

import threading
class Singleton(object):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        pass
    @staticmethod
    def getInstance():
        if not Singleton.__instance:
            Singleton.__lock.acquire()
            if not Singleton.__instance:
                Singleton.__instance = object.__new__(Singleton)
                object.__init__(Singleton.__instance)
            Singleton.__lock.release()
        return Singleton.__instance

