__author__ = 'fanyunlei'
from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType

class User(LadonType):
        name = unicode
        age = int
        groups = [ unicode ]

class ListUsersResponse(LadonType):
        success = bool
        users = [ User ]

class UserService(object):

        @ladonize(unicode,rtype=ListUsersResponse)
        def listUsers(self,uid):

                user1 = User()
                user1.name = u"John Doe"
                user1.age = 30
                user1.groups = [ u'admin', u'www-data' ]

                user2 = User()
                user2.name = u"John Deer"
                user2.age = 60
                user2.groups = [ u'farming', u'tractor' ]

                result = ListUsersResponse()
                result.success = True
                result.users = [ user1, user2 ]

                return result
