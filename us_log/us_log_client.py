#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
if len(sys.argv) != 2:
    print 'usage: python %s <command>' % sys.argv[0]
    sys.exit(0)
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect("/tmp/UNIX.d")
sock.send(sys.argv[1])
print sock.recv(1024)
sock.close()
