import socket

packet_num = 0


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('192.168.1.3',12347)) #connect to server's ip and a port number

socket.listen(5) # the server listens to the clients

while True:
     
     msg=packet_num
     sock.send(msg.encode('utf-8'))
     
     data=sock.recv(1024) #the 1024 is the buffer size
     print(data.decode())
     packet_num+=1