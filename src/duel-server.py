import re
from cgi import escape, parse_qs

# boilerplate code from the internet, enchanced hello-word for mod_wsgi

def index(environ, start_response, url):
    """This function will be mounted on "/" and display a link
    to the hello world page."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['TK YOU CUNT']

def hello(environ, start_response, url):
    """Like the example above, but it uses the name specified in the
URL."""
    # get the name from the url if it was specified there.
    args = environ['myapp.url_args']
    qs = parse_qs(environ['QUERY_STRING'])

    if 'name' in qs:
        subject = escape(qs['name'][0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hi %ss! - %s' % (subject, environ.__str__())]

def not_found(environ, start_response, url):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['serving nothing at %s, sorry.' % url]

# map urls to functions
urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello)
]

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    environ['post'] = environ['wsgi.input'].read()
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response, path)
    return not_found(environ, start_response, path)

