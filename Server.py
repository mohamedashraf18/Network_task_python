import socket

packet_count = 0
packet_list = ["First", "second", "third", "Fourth"]

server_ip = socket.gethostbyname(socket.gethostname())
server_port = 12347
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((server_ip, server_port))
print("UDP server started")
print("IP and Port: ", server_ip, " ", server_port)

while packet_count != -1:
    # Receive packet number from a device and save its address
    received = server_socket.recvfrom(1024)
    packet_count = int.from_bytes(received[0], byteorder="big")
    client_add = received[1]

    print("Received {} from {}".format(packet_count, client_add))

    # send corresponding packet to client
    server_socket.sendto(packet_list[packet_count].encode(), client_add)

server_socket.close()
