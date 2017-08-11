import socket

shutdown = False

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 0
s.bind((host, port))
s.setblocking(0)

server = (host, 5000)

nickname = raw_input("Your nickname:")
message = raw_input(nickname + " --->")

while message != "exit":
    if message != "":
        s.sendto(nickname + ":" + message, server)
    message = raw_input(nickname + " --->")

shutdown = True
s.close()
