import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipAddress = input("Input your receiver IP Address: ")

client.connect((ipAddress, 8080))

def send_message():
    while True:
        print("")
        print("HaloDek!")
        print("---------------------------------")
        print("Try send some message to your friend")
        print("---------------------------------")
        message = input()
        client.send(message.encode())

# Local receiver
# def receive_message():
#     while True:
#         try:
#             message = client.recv(1024)
#             print("New message received : ", message.decode())
#             print("---------------------------------")
#             print("")
#         except:
#             break


send_thread = threading.Thread(target=send_message)
# receive_thread = threading.Thread(target=receive_message) <-- local receiver

send_thread.start()
# receive_thread.start() <-- local receiver