#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description   客户端/服务器  以及TCP和UDP编程
from socket import *
from time import ctime

HOST=''
PORT=21667
ADDR = (HOST, PORT)
BUFSIZ = 1024

udpserver = socket(AF_INET, SOCK_DGRAM)
udpserver.bind(ADDR)

while True:
    print 'waiting for message'
    data,addr = udpserver.recvfrom(BUFSIZ)
    udpserver.sendto('[%s] %s' %(ctime(), data), addr)

    print '...received from',addr
udpserver.close()