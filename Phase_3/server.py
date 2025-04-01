import socket
import threading

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the sever to your computer ip and a desired port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# put it on listen (for incoming connection)
server_socket.listen()

#a dictionary for clients
clients = dict()

def leave_message(name,address):
    print(f"{name} ({address}) has left the server")

def broadcast(message):
    """show the messages for everyone"""
    for client in clients.keys():
        client.send(message)


def receive_message(client_socket):
    """receive message from client"""

    while True:
        address = str(client_socket)[-26:-3]
        # we need a try except so that our program doesn't crash
        try:
            #receive the message from the client
            message = client_socket.recv(1024).decode("utf-8")
            if message.lower() == "/exit":
                raise Exception("Client requested to disconnect")  # This will trigger the except block
            message = f"\033[1;34m\n\t{clients[client_socket]} ({address}): {message}\n\033[0m".encode("utf-8")
            #show the message to everyone
            broadcast(message)
        except:
            #name of client
            name = clients[client_socket]
            #remove the client from the dictionary
            clients.pop(client_socket)
            #close the connection for the client
            client_socket.close()
            #let others know that the client left the server
            broadcast(f"\033[1;31m\n\t{name} ({address}) has left the server\n\033[0m".encode("utf-8"))
            leave_message(name, address)
            print("*" * 30)
            break


def connect_client():
    """connecting to server"""
    while True:

        #accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"connected to {client_address}")
        print("*" * 30)

        #request for client name
        username_code = "ajlskdfdfdfjaslfkj"
        client_socket.send(f"ajlskdfdfdfjaslfkj".encode('utf-8'))
        client_name = client_socket.recv(1024).decode('utf-8')

        #adding the client to dictionary
        clients.update({client_socket: client_name})
        print(f"client name: {clients[client_socket]}")
        print("*" * 30)

        #informing the client
        client_socket.send(f"\nwelcome {clients[client_socket]}, you are connected to the server\n".encode('utf-8'))
        broadcast(f"{clients[client_socket]} has joined the server".encode("utf-8"))

        #when a client connects to the server stat a thread
        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()

#set up the server
print()
print("*" * 30)
print("server is looking for connection...")
print("*" * 30)
connect_client()

