import socket

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the sever to your computer ip and a desired port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# put it on listen (for incoming connection)
server_socket.listen()

#a dictionary for clients
clients = {}

def noting():
    print()
    print("*" * 30)
    print("server is looking for connection...")
    print("*" * 30)
    print()

def connect():
    """connecting to server"""

    while True:

        #accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"connected to {client_address}")

        #request for client name
        client_socket.send(f"what is your name? ".encode('utf-8'))
        client_name = client_socket.recv(1024).decode('utf-8')

        #adding the client to dictionary
        clients[client_socket] = client_name
        print(f"new client: {clients[client_socket]}")

        #informing the client
        client_socket.send(f"welcome {clients[client_socket]}, you are connected to the server\n".encode('utf-8'))

#set up the server
noting()
connect()

