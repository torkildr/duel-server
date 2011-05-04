#!/usr/bin/env python

import cgi

from WsgiInterface import *

def get_hello(request):
    return Response("Hi there, %s!" % (request.username))

def get_dump(request):
    data = []

    for (key, val) in request.env.iteritems():
        try:
            data.append("%s = %s" % (key, cgi.escape(val.__str__())))
        except AttributeError:
            data.append("%s = N/A" % (key))

    return Response("<br>\n".join(data), type=ContentType.HTML)

