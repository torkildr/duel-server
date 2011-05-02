#!/usr/bin/env python

import cgi

from WsgiInterface import *

def get_hello(request):
    return Response("Hi there!")

def get_dump(request):
    data = []

    for (key, val) in request.env.iteritems():
        try:
            data.append("%s = %s" % (key, cgi.escape(val.__str__())))
        except AttributeError:
            data.append("%s = MONGO!" % (key))

    return Response("<br>\n".join(data), type=ContentType.HTML)

def not_found(request):
    return Response('serving nothing at %s, sorry.' % request.env['PATH_INFO'], code=StatusCode.NOT_FOUND)

