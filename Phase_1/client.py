#importing the socket module
import socket

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server with specified ip address (your computer ip) and port number
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

#infinite loop for sending and receiving messages
while True:

    # receiving information from the server (buffer size is 1024)
    message = client_socket.recv(1024).decode("utf-8")

    # quiting if the connected client wants to quit else keep sending messages
    if message.lower() == "quit":
        client_socket.send("quit".encode("utf-8"))
        break
    else:
        print(message)
        message = input("message: ")
        client_socket.send(message.encode("utf-8"))

#if we quit from the server
client_socket.close()