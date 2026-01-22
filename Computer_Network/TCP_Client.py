import socket

HOST = '127.0.0.1'  # Server IP
PORT = 65432        # Server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))               # Connect to server
    s.sendall(b'Hello, TCP Server!')      # Send data
    data = s.recv(1024)                   # Receive response
    print('Received from server:', data.decode())
