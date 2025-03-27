#importing the socket module
import socket

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the sever to your computer ip and a desired port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# put it on listen (for incoming connection)
server_socket.listen()

#accept incoming connections
client_socket, client_address = server_socket.accept()

#infinite loop for sending and receiving messages
while True:

    # receiving information from the server (buffer size is 1024)
    message = client_socket.recv(1024)

    # quiting if the connected client wants to quit else keep sending messages
    if message.lower() == "quit":
        client_socket.send(b"quit")
        break
    else:
        print(str(message)[2:-1])
        message = input("message: ")
        client_socket.send(message.encode("utf-8"))

#closing the server socket
server_socket.close()

