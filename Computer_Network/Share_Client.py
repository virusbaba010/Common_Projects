import socket

def send_tcp(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(filename, "rb") as f:
            while True:
                bytes_data = f.read(4096)
                if not bytes_data:
                    break
                s.sendall(bytes_data)
        print("File sent via TCP")

def send_udp(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        with open(filename, "rb") as f:
            while True:
                bytes_data = f.read(4096)
                if not bytes_data:
                    break
                s.sendto(bytes_data, (host, port))
        print("File sent via UDP")

host = "127.0.0.1"
port = 12345
filename = "data.txt"
conn_type = input("Choose connection (TCP/UDP): ").strip().upper()

if conn_type == "TCP":
    send_tcp(filename, host, port)
elif conn_type == "UDP":
    send_udp(filename, host, port)
else:
    print("Invalid option!")
