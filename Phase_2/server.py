import socket
import threading

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the local machine's IP and port 12345
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Listen for incoming connections
server_socket.listen()
print("Server is waiting for connections...\n")
clients = []

def handle_client(client_socket, client_address):
    """Handles communication with a connected client"""
    print(f"{client_address} connected to the server")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break  # Client disconnected

            print(f"{client_address}: {message}")

            # Send confirmation back to the client
            confirmation = f"You sent ({message})"
            client_socket.sendall(confirmation.encode("utf-8"))

        except:
            break

    print(f"{client_address} left the server\n")
    clients.remove(client_socket)
    client_socket.close()

def accept_clients():
    """Accepts new client connections"""
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

# Start accepting clients
accept_clients()
