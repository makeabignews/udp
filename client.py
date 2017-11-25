from socket import socket, AF_INET, SOCK_DGRAM
def send(msg,addr,port):
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(msg, (addr, 3000))
    re_msg, addr = s.recvfrom(3001)
    print re_msg
send('21_on','localhost',3000)