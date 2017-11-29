from socket import socket, AF_INET, SOCK_DGRAM
def send(msg,addr,port,size):
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(msg, (addr, port))
    re_msg, addr = s.recvfrom(size)
    print re_msg
send('hello','192.168.2.22',1337,200)