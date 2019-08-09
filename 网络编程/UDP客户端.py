#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description
from socket import *
from  time import  ctime
HOST='localhost'
PORT=21667
BUFSIZ=1024
ADDR=(HOST, PORT)

udpclisock = socket(AF_INET, SOCK_DGRAM)

while True:
    data=raw_input('>')
    if not data:
        break
    udpclisock.sendto(data,ADDR)
    data,ADDR = udpclisock.recvfrom(BUFSIZ)
    print  data
    if not data:
        break
udpclisock.close()