#!/usr/bin/python
# -*- coding:UTF-8 -*-
from socket import socket, AF_INET, SOCK_DGRAM
import time


def save(filename,txt):
    try:
        fobj=open(filename,'a')                 # 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
    except IOError:
        print '*** file open error:'
    else:
        fobj.write('\n'+txt)   #  这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
        fobj.close()                              #   特别注意文件操作完毕后要clos
def udp_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(500)
        print('message:%s from %s' % (msg, addr))
        resp = time.ctime()
        #sock.sendto(resp.encode('ascii'), addr)
        state="ok"
        sock.sendto(state, addr)
        txt="\ntime:%s \nmsg:%s\n```" % (resp,msg)
        save("/home/makeabignews/msg.md",txt)
        

if __name__ == '__main__':
    udp_server(('', 3000))