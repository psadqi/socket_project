import socket
import threading

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the local machine's IP and port 12345
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Listen for incoming connections
server_socket.listen()
print("Server is waiting for connections...\n")

#list of clients
clients = []

def handle_client(client_socket, client_address):
    """Handles communication with a connected client"""

    #let the client know he is connected to the server and add him to the list
    print(f"{client_address} connected to the server")
    clients.append(client_socket)

    while True:
        #try except for any possible errors
        try:
            #receive the message and show it on server side
            message = client_socket.recv(1024).decode("utf-8")

            #/exit for leaving the server
            if message.lower() == "/exit":
                break

            print(f"{client_address}: {message}")

            # Send clients message back to himself
            clients_message = f"You sent ({message})"
            client_socket.send(clients_message.encode("utf-8"))

        except:
            break

    print(f"!!! {client_address} left the server !!!\n")
    #remove the client from the list and close the connection
    clients.remove(client_socket)
    client_socket.close()

def connect_client():
    """connecting to server"""
    while True:
        #accepting the client
        client_socket, client_address = server_socket.accept()

        #make a thread so any clients can connect and send as many messages as they wants
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

# Start accepting clients
connect_client()
