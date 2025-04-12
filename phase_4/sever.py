import socket
import threading

# Creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to your computer ip and a desired port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Put it on listen (for incoming connection)
server_socket.listen()

# A dictionary for clients (stores both name and color)
clients = dict()


def broadcast(message):
    """Show the messages for everyone"""
    for client in clients.keys():
        try:
            client.send(message)
        except:
            # Remove broken connections
            clients.pop(client)


def receive_message(client_socket):
    """Receive message from client"""
    while True:
        address = str(client_socket)[-26:-3]
        try:
            # Receive the message from the client
            message = client_socket.recv(1024).decode("utf-8")
            if message.lower() == "/exit":
                raise Exception

            # Get client info from dictionary
            client_name, client_color = clients[client_socket]

            # Format: "username|color|message"
            formatted_message = f"{client_name}|{client_color}|{message}"
            broadcast(formatted_message.encode("utf-8"))

        except:
            # Name and color of client
            if client_socket in clients:
                client_name, client_color = clients[client_socket]
                # Remove the client from the dictionary
                clients.pop(client_socket)
                # Close the connection for the client
                client_socket.close()
                # Let others know that the client left the server
                broadcast(f"{client_name}|{client_color}|has left the server".encode("utf-8"))
                print(f"{client_name} ({address}) has left the server.")
                print("*" * 30)
            break


def connect_client():
    """Connecting to server"""
    while True:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"{client_address} has connected.")
        print("*" * 30)

        try:
            # Request for client name and color
            client_info = client_socket.recv(1024).decode('utf-8').split('|')
            client_name = client_info[0]
            client_color = client_info[1] if len(client_info) > 1 else "black"

            # Validate color
            valid_colors = ["black", "red", "green", "blue"]
            if client_color not in valid_colors:
                client_color = "black"

            # Adding the client to dictionary
            clients.update({client_socket: (client_name, client_color)})
            print(f"client: {client_name} ({str(client_socket)[-27:-1]}) with color {client_color}")
            print("*" * 30)

            # Informing the client
            client_socket.send(f"welcome {client_name}, you are connected to the server.".encode('utf-8'))
            broadcast(f"{client_name}|{client_color}|has joined the server".encode("utf-8"))
        except:
            print(f"({str(client_socket)[-25:-2]}) has left the server.")
            print("*" * 30)
            continue

        # When a client connects to the server start a thread
        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()


# Set up the server
print()
print("*" * 30)
print("server is looking for connection...")
print("*" * 30)
connect_client()