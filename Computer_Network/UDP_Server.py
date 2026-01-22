import socket

UDP_IP = "192.168.88.219"   # Localhost
UDP_PORT = 5005        # Port to listen on

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)            # Buffer size is 1024 bytes
    print(f"Received packet from {addr}: {data.decode('utf-8')}")
    sock.sendto("Message received".encode(), addr)   # Send response
