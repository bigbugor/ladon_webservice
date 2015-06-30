__author__ = 'big_buger'
from ladon.ladonizer import ladonize

class Calculator(object):

        @ladonize(int,int,rtype=int)
        def add(self,a,b):
                print("+++++++++++++++++++")
                return a+b
