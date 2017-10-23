#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import signal
import logging

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

def set_log_error(a, b):
    print a, b, 'set error'
    LOG.setLevel(logging.ERROR)

def set_log_debug(a, b):
    print a, b, 'set debug'
    LOG.setLevel(logging.DEBUG)

signal.signal(signal.SIGUSR1, set_log_error)
signal.signal(signal.SIGUSR2, set_log_debug)

while True:
    LOG.error('11111111111')
    LOG.warn('22222222222')
    LOG.info('33333333333')
    LOG.debug('44444444444')
    time.sleep(1)
