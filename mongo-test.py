#!/usr/bin/env python

from pymongo import Connection

import time

connection = Connection()
db = connection.duel

class User(object):
    def __init__(self, username):
        self.username = username
        self.timestamp = time.time();

    @property
    def id(self):
    	return self.username

    @property
    def time(self):
    	return self.timestamp

result = db.users.find({"id" : "markild"})

if not result:
    print "Inserting..."
    user = User("markild")
    db.users.insert({"id" : user.id, "time" : user.time})
    result = db.users.find({"id" : "markild"})

print "Fetching..."
for user in result:
    print user

