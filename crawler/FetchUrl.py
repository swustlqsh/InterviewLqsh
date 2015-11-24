#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'qiusheng'
# email: qiushengli245@gmail.com

import threading
import Queue
import time

'''
 简单线程池的设计
 1. 线程池管理器 (ThreadPool) 用于启动 停用 管理线程池
 2. 工作线程 (WorkThread) 线程池中被激活的线程
 3. 请求接口 (WorkRequest) 创建请求对象，供工作线程调度执行
 4. 请求队列 (RequestQueue) 用于存放请求和提取请求
 5. 结果队列 (ResultQueue) 用于存储请求之后的返回结果
'''






class FetchUrl(threading.Thread):
    pass
