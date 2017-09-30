#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
import os
if os.path.exists('/tmp/UNIX.d'):
    os.unlink('/tmp/UNIX.d')
sock.bind('/tmp/UNIX.d')
sock.listen(5)
while True:
    connection,address = sock.accept()
    print "Data : %s"%connection.recv(1024)
    connection.send("hello")
    connection.close()
