import socket

UDP_IP = "127.0.0.1"    # Destination IP
UDP_PORT = 5005         # Destination port

message = "Hello, UDP!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
data, server_address = sock.recvfrom(1024)          # Receive response
print(f"Received response from server: {data.decode()}")
sock.close()
