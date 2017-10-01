#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import signal
import logging
import threading


# 指定打印日志的级别
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='../demo.log',
        filemode='a'
)

# 输出到控制台的日志与级别
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)

LOG = logging.getLogger('')
LOG.addHandler(console)


class Listener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 监听socket文件
        import socket
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        import os
        if os.path.exists('/tmp/UNIX.d'):
            os.unlink('/tmp/UNIX.d')
        sock.bind('/tmp/UNIX.d')
        sock.listen(5)
        while True:
            conn,address = sock.accept()
            data = conn.recv(1024)
            if data == 'error':
                LOG.setLevel(logging.ERROR)
            elif data == 'warn':
                LOG.setLevel(logging.WARNING)
            elif data == 'info':
                LOG.setLevel(logging.INFO)
            elif data == 'debug':
                LOG.setLevel(logging.DEBUG)
            conn.send("OK")
            conn.close()

t = Listener()
t.setDaemon(True)
t.start()
#t.join()

while True:
    LOG.error('11111111111')
    LOG.warn('22222222222')
    LOG.info('33333333333')
    LOG.debug('44444444444')
    time.sleep(1)
