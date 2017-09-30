#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect("/tmp/UNIX.d")
sock.send('hello')
print sock.recv(1024)
sock.close()
