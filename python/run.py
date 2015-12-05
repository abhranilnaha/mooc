#-------------------------------------------------------------------------------
# Name:        run
# Purpose:
#
# Author:      anaha
#
# Created:     12/05/2015
# Copyright:   (c) anaha 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Client import MoocClient

if __name__ == '__main__':
  import sys
  if len(sys.argv) != 3:
    print "Usage: python run.py <host> <port>"
  else:
    host = sys.argv[1]
    port = int(sys.argv[2])
    mooc =  MoocClient()
    mooc.connect(host,port)
    mooc.makePingRequest()
    mooc.makeSignUpRequest()