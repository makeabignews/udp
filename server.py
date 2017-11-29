from socket import socket, AF_INET, SOCK_DGRAM
import time

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

if __name__ == '__main__':
    udp_server(('', 3000))