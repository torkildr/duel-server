#!/usr/bin/env python

from wsgiref.simple_server import make_server
import random, sys, Duel

try:
    port = int(sys.argv[1])
except:
    port = random.randint(5001, 5999)

httpd = make_server('', port, Duel.application)

print "Serving HTTP on port %d ..." % (port)

# Respond to requests until process is killed
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print "\nShutting down..."

# Alternative: serve one request, then exit
#httpd.handle_request()

