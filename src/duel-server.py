import re
from cgi import escape, parse_qs

import sys
sys.path.append('/var/http/duel-server/src') # TODO

log = open('/tmp/duellog', 'wa')

import duel_api

"""
    URL syntax is as follows:
    <root>/<userid>/action
"""
# modify record (idempotent)
put_handlers = {}

# get record (non-modifying, idempotent)
get_handlers = { 'index' : duel_api.get_index,
                 'hello' : duel_api.get_hello,
                 'goodbye' : duel_api.get_goodbye,
                 'dump' : duel_api.get_dump
               }

# create record
post_handlers = {}

# delete record (idempotent)
delete_handlers = {}

# not found
not_found = duel_api.not_found

handlers = {'GET' : get_handlers,
            'POST' : post_handlers,
            'DELETE': delete_handlers,
            'PUT' : put_handlers
            }

# boilerplate code from the internet, enchanced hello-word for mod_wsgi
def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the correct handlers

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    req = path.split('/')

    try:
        user = req[0]
        action = req[1]
        rest = req[2:]
    except:
        return not_found(environ, start_response, None, None)

    method = environ['REQUEST_METHOD']
    environ['duel.postdata'] = environ['wsgi.input'].read()

    if not method in handlers:
        return not_found(environ, start_response, user, rest)

    if not action in handlers[method]:
        return not_found(environ, start_response, user, rest)

    return handlers[method][action](environ, start_response, user, rest)

