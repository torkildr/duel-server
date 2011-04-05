#!/usr/bin/env python

from pymongo import Connection
from pymongo.son_manipulator import SONManipulator

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
print result

if result:
    print "Fetching..."
    for user in result:
    	print user
else:
    print "Inserting..."
    user = User("markild")
    db.users.insert({"id" : user.id, "time" : user.time})

