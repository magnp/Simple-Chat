import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 5000
s.bind((host, port))

clients = []
print "Server started. Begin chat.";

while True:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        for client in clients:
            s.sendto(data, client)

    except:
        pass

s.close()
