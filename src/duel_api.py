import cgi

def get_index(environ, start_response, user, args):
    """This function will be mounted on "/" and display a link
    to the hello world page."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['index\n']

def get_goodbye(environ, start_response, user, args):
    # get the name from the url if it was specified there.
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Cya %s!\n' % user]

def get_hello(environ, start_response, user, args):
    # get the name from the url if it was specified there.
    qs = cgi.parse_qs(environ['QUERY_STRING'])

    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hi %s!\n' % user]

def get_dump(environ, start_response, user, args):
    # dump everything
    # qs = cgi.parse_qs(environ['QUERY_STRING'])

    start_response('200 OK', [('Content-Type', 'text/html')])
    path = '/'.join([user] + args)
    env = '<br>\n'.join(["%s=%s" % (x,cgi.escape(y.__str__())) for x,y in environ.iteritems()])
    return ['Data for: ' + path + '\n<br>' + env]

def not_found(environ, start_response, user, args):
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['serving nothing at %s, sorry.' % environ['REQUEST_URI']]
