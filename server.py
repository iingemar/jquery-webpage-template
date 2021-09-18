#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

"""
# Is server running?
# 11582 pts/0    S      0:00 python server.py
# 31970 pts/1    S+     0:00 grep server.py
ps ax | grep server.py

# Destroy
kill 11582

# Start server
nohup python server.py &

"""
PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()