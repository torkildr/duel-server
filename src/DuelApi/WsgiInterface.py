#!/usr/bin/evn python

class ContentType:
    # text
    PLAIN = "text/plain"
    HTML = "text/html"
    # data formats
    XML = "application/xml"
    JSON = "application/json"

class StatusCode:
    # a-ok
    OK = "200 OK"
    # redirect
    MOVED = "301 Moved"
    # client error
    BAD_REQUEST = "400 Bad request"
    UNAUTHORIZED = "401 Unauthorized"
    FORBIDDEN = "403 Forbidden"
    NOT_FOUND = "404 Not found"
    # server errror
    ERROR = "500 Internal Error"
    NOT_IMPLEMENTED = "501 Not implemented"


class Request(object):
    def _get_env(self, key, default=None):
        if self.env.has_key(key):
            return self.env[key]
        return default

    def __init__(self, env):
        self.env = env

        path = self._get_env("PATH_INFO")

        if path:
            self.path = path.lstrip("/").split("/")
        else:
            self.path = []

    @property
    def method(self):
        return self._get_env('REQUEST_METHOD')

    @property
    def action(self):
        return self.path[0]


class Response(object):
    def __init__(self, data, code = StatusCode.OK, type = ContentType.PLAIN):
        self.data = data
        self.code = code
        self.type = type

    def httpResponse(self, start_response):
        start_response(self.code, [('Content-Type', self.type)])

        return [self.data]

