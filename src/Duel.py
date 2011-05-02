#!/usr/bin/env python

import re
import sys

from DuelApi import *
from DuelApi.WsgiInterface import *

log = open('/tmp/duel-server.log', 'wa')

"""
    URL syntax is as follows:
    <root>/<userid>/action
"""

# modify record (idempotent)
put_handlers = {}

# get record (non-modifying, idempotent)
get_handlers = {
    'hello' : Api.get_hello,
    'dump'  : Api.get_dump
}

# create record
post_handlers = {}

# delete record (idempotent)
delete_handlers = {}

handlers = {
    'GET' : get_handlers,
    'POST' : post_handlers,
    'DELETE': delete_handlers,
    'PUT' : put_handlers
}

# application entry point, handles requests
def application(environment, start_response):
    request = Request(environment)

    if not request.method in handlers:
        response = Api.not_found(request)
        return response.httpResponse(start_response)

    if not request.action in handlers[request.method]:
        response = Api.not_found(request)
        return response.httpResponse(start_response)

    response = handlers[request.method][request.action](Request(environment))
    return response.httpResponse(start_response)

