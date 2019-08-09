#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description
from   socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpclisock=socket(AF_INET, SOCK_STREAM)
tcpclisock.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    tcpclisock.send(data)
    data = tcpclisock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpclisock.close()