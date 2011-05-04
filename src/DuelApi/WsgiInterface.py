#!/usr/bin/env python

class ContentType:
    # text
    PLAIN = 'text/plain'
    HTML = 'text/html'
    # data formats
    XML = 'application/xml'
    JSON = 'application/json'

class StatusCode:
    # a-ok
    OK = '200 OK'
    # redirect
    MOVED = '301 Moved'
    # client error
    BAD_REQUEST = '400 Bad request'
    UNAUTHORIZED = '401 Unauthorized'
    FORBIDDEN = '403 Forbidden'
    NOT_FOUND = '404 Not found'
    # server errror
    ERROR = '500 Internal Error'
    NOT_IMPLEMENTED = '501 Not implemented'

# this contains all information related to the web request
class Request(object):
    def _get_env(self, key, default=None):
        if key in self.env:
            return self.env[key]
        return default

    def __init__(self, env):
        self.env = env

        path = self._get_env('PATH_INFO', '')[1:].split('/')

        # makes sure that empty path-elements are marked as such
        if path:
            self.path = [x if x else None for x in path]
        else:
            self.path = []

    @property
    def method(self):
        return self._get_env('REQUEST_METHOD')

    @property
    def username(self):
        try:
            return self.path[0]
        except:
            return None

    @property
    def action(self):
        try:
            return self.path[1]
        except:
            return None

    @property
    def query(self):
        return self.path[2:]

# here we put all information that is related to the response we later
# will send to the client
class Response(object):
    def __init__(self, data, code = StatusCode.OK, type = ContentType.PLAIN):
        self.data = data
        self.code = code
        self.type = type
        self.headers = [('Content-Type', self.type)]

    # adds a header to the response, is not sent until httpResponse is
    # called
    def addHeader(self, header, value):
        self.headers.append((header, value))

    # because of headers and such, we will probably want to delay the
    # sending of repsone for a good while.
    def httpResponse(self, start_response):
        start_response(self.code, self.headers)

        return [self.data]

