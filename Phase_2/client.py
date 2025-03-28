import socket

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server with specified ip address (your computer ip) and port number
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))