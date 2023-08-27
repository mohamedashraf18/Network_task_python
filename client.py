import socket

packet_num = 0


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('192.168.1.19', 12347)) #connect to server's ip and a port number

while True:
    # Transform packet num to bytes
     msg=packet_num
     sock.send(msg.to_bytes(4, byteorder="big"))
     
     data=sock.recv(1024) #the 1024 is the buffer size
     print(data.decode())

     # Terminate program after last packet
     if data.decode() == "Connection terminated":
          break

     packet_num+=1
