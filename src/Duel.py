#!/usr/bin/env python

import re
import sys

from DuelApi import Api
from DuelApi.WsgiInterface import *

"""
    URL syntax is as follows:
    <root>/action
"""

# get record (non-modifying, idempotent)
get_handlers = {
    'hello' : Api.get_hello,
    'dump'  : Api.get_dump
}

# modify record (idempotent)
put_handlers = {}

# create record
post_handlers = {}

# delete record (idempotent)
delete_handlers = {}

handlers = {
    'GET' : get_handlers,
    'HEAD' : get_handlers,
    'POST' : post_handlers,
    'DELETE': delete_handlers,
    'PUT' : put_handlers
}

# application entry point, handles requests
def application(environment, start_response):
    request = Request(environment)

    # no username
    if not request.username:
        response = Response("No username given", code=StatusCode.BAD_REQUEST)
        return response.httpResponse(start_response)

    # no method mapped
    if not request.method in handlers or not request.action in handlers[request.method]:
        response = Response("No such method", code=StatusCode.BAD_REQUEST)
        return response.httpResponse(start_response)

    # dispatch the request
    response = handlers[request.method][request.action](Request(environment))
    return response.httpResponse(start_response)

