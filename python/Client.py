#-------------------------------------------------------------------------------
# Name:        Client
# Purpose:
#
# Author:      anaha
#
# Created:     12/05/2015
# Copyright:   (c) anaha 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from SocketChannel import SocketChannel, SocketChannelFactory
from comm_pb2 import Request, Header, CourseOperation, CourseDesc, NameValueSet

class MoocClient():

  def __init__(self):
    self.channelFactory = SocketChannelFactory()

  def validateMessage(self, protobufMsg):
    '''
    Check the protobuf message
    '''
    if not protobufMsg.IsInitialized():
        raise Exception("Invalid message")

  def connect(self, host="localhost", port=5570):
    self.channel = self.channelFactory.openChannel(host,port)
    print "Connection successful"

  def close(self):
    if self.channel:
        self.channel.close()

  def send(self, request):
    # Check if channel is connected
    if not self.channel.connected:
        openChannel()

    self.channel.write(request.SerializeToString())
    print "send successful"

  def makeSignUpRequest(self):
    request = Request()
    request.header.originator = "client"
    request.header.routing_id = Header.COURSES

    request.body.course_op.action = CourseOperation.ADDCOURSE
    request.body.course_op.data.name_space = "sign_up"
    request.body.course_op.data.owner_id = 8888
    request.body.course_op.data.course_id = "signup"
    request.body.course_op.data.status = CourseDesc.COURSEUNKNOWN

    data = request.body.course_op.data
    data.options.node_type = NameValueSet.VALUE
    data.options.name = "email"
    data.options.value = "abhranilnaha@gmail.com"

    self.send(request)
    print "signup successful"

  def makePingRequest(self):
    request = Request()
    request.header.originator = "client"
    request.header.routing_id = Header.PING

    request.body.ping.number = 3
    request.body.ping.tag = "python-client"

    self.send(request)
    print "ping successful"
