import socket

def server_tcp(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        s.listen(1)
        conn, addr = s.accept()
        with conn, open("received_tcp.txt", "wb") as f:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
        print("File received via TCP")

def server_udp(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", port))
        with open("received_udp.txt", "wb") as f:
            while True:
                data, addr = s.recvfrom(4096)
                if not data:
                    break
                f.write(data)
        print("File received via UDP")

port = 12345
conn_type = input("Choose server type (TCP/UDP): ").strip().upper()

if conn_type == "TCP":
    server_tcp(port)
elif conn_type == "UDP":
    server_udp(port)
else:
    print("Invalid option!")
