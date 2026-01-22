import socket

# Server configuration
HOST = '10.23.198.90'  # Localhost
PORT = 7457       # Port to listen on

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))     # Bind socket to address and port
    s.listen()               # Listen for incoming connections
    
    print('Server is listening...')


    conn, addr = s.accept()  # Accept a connection
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # Receive data
            if not data:
                break
            print("Received:", data.decode())
            conn.sendall(data)      # Echo back received data
