import socket
import threading

# inisialisasi server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 12345))

server.listen(5)
print("Server is listening...")

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if clients != client_socket:
            try:
                client.send(message)
            except:
                client.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Message received: {message.decode()}")
                broadcast(message, client_socket)
            else:
                clients.remove(client_socket)
        except:
            break

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    print(f"Connected with: {client_address}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()