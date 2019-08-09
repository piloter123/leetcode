#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description   客户端/服务器  以及TCP和UDP编程
'''
 服务器存在的唯一目的就是等待客户端的请求，并响应他们（提供服务），然后等待更多请求。
 客户端因特定请求而联系服务器，等待服务器响应，客户端可能在一段时间内再次发出其他请求，但是被当作不同的事务。
 打印机相当于硬件服务器，软件服务器也运行在硬件服务器之上，主要有Web服务器
 TCP基于流套接字，UDP基于数据包类型的套接字
'''
from  socket import *
from time   import  ctime


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSocK=socket(AF_INET, SOCK_STREAM)
tcpSocK.bind(ADDR)
tcpSocK.listen(4)
while True :
    print 'waiting for connection'
    tcpclisock ,addr = tcpSocK.accept()
    print '...connect from :' , addr
    while True:
        data = tcpclisock.recv(BUFSIZ)
        if not data:
            break
        tcpclisock.send('[%s] %s'%(ctime(), data ))
    tcpclisock.close()
tcpSocK.close()