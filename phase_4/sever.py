# Import the required modules
import socket     # For network communication (creating a server and connecting clients)
import threading  # For handling multiple clients simultaneously using threads
from datetime import datetime

# Create a TCP/IP socket using IPv4 addressing
# AF_INET = IPv4, SOCK_STREAM = TCP (connection-based)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the local IP address and a port number (12345 in this case)
# This allows the server to receive connections on this IP and port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Set the socket to listen mode to accept incoming connection requests
server_socket.listen()

# Create an empty dictionary to store connected clients
# Each client is associated with their socket and a tuple containing (name, color)
clients = dict()

# Add near the clients dictionary (Page 1)
username_to_socket = {}  # Maps usernames to their sockets


def broadcast(message):
    """
    Send a message to all connected clients.
    This is used for public messages that should be seen by everyone.
    """
    for client in clients.keys():
        try:
            # Attempt to send the message to the client
            client.send(message)
        except:
            # If an error occurs (e.g., client disconnected), remove them from the list
            clients.pop(client)


def receive_message(client_socket):
    """
    Continuously receive messages from a client.
    If the message is '/exit', disconnect the client.
    """
    while True:
        # Extract the client address string (for display/logging)
        address = str(client_socket)[-26:-3]
        try:
            # Receive data from the client (up to 1024 bytes) and decode it
            message = client_socket.recv(1024).decode("utf-8")

            # Handle private messages (format: "/pm <username> <message>")
            if message.startswith("/pm "):
                parts = message.split(" ", 2)  # Split into ["/pm", "username", "message"]
                if len(parts) == 3:
                    target_username, pm_content = parts[1], parts[2]
                    sender_name, _ = clients[client_socket]

                    # Send PM only to the target user
                    if target_username in username_to_socket:
                        target_socket = username_to_socket[target_username]
                        target_socket.send(
                            f"[PM from {sender_name}] {pm_content}".encode("utf-8")
                        )
                        # Optional: Confirm delivery to sender
                        client_socket.send(f'{sender_name}: {pm_content} ({datetime.now().strftime("%H:%M")})'.encode("utf-8"))
                    else:
                        client_socket.send(f"User '{target_username}' not found.".encode("utf-8"))
                continue

            # If the client types '/exit', treat it as a disconnect request
            if message.lower() == "/exit":
                raise Exception

            # Retrieve client's name and color from the dictionary
            client_name, client_color = clients[client_socket]

            # Format the message with the client's name and color for UI rendering
            formatted_message = f"{client_name}|{client_color}|{message}"

            # Send the message to all connected clients
            broadcast(formatted_message.encode("utf-8"))

        except:
            # Handle client disconnection
            if client_socket in clients:
                # Get client name and color
                client_name, client_color = clients[client_socket]

                # Remove the client from the clients dictionary
                clients.pop(client_socket)

                # Close the client connection
                client_socket.close()

                # Notify all other clients that this client has left the chat
                broadcast(f"{client_name}|{client_color}|has left the server".encode("utf-8"))

                # Log the disconnection on the server side
                print(f"{client_name} ({address}) has left the server.")
                print("*" * 30)
            break


def connect_client():
    """
    Wait for new client connections.
    For each connection:
    - Receive client's name and color
    - Add them to the clients dictionary
    - Notify others
    - Start a new thread to receive messages from that client
    """
    while True:
        # Accept an incoming connection, returns a socket object and address
        client_socket, client_address = server_socket.accept()

        # Log the new connection
        print(f"{client_address} has connected.")
        print("*" * 30)

        try:
            # Receive client's name and color preference, separated by '|'
            client_info = client_socket.recv(1024).decode('utf-8').split('|')
            client_name = client_info[0]
            client_color = client_info[1] if len(client_info) > 1 else "black"

            # Add to username-to-socket mapping
            username_to_socket[client_name] = client_socket

            # Define allowed colors
            valid_colors = ("black", "red", "green", "blue")

            # If color is not valid, assign default (black)
            if client_color not in valid_colors:
                client_color = "black"

            # Store client data in the dictionary
            clients.update({client_socket: (client_name, client_color)})

            # Log client details on the server side
            print(f"client: {client_name} {str(client_socket)[-27:-1]} with color {client_color}")
            print("*" * 30)

            # Send a welcome message to the client
            client_socket.send(f"welcome {client_name}\n".encode('utf-8'))

            # Broadcast to everyone that a new client has joined
            broadcast(f"{client_name}|{client_color}|has joined the server".encode("utf-8"))

        except:
            # If any error occurs during client info reception, disconnect them
            print(f"({str(client_socket)[-25:-2]}) has left the server.")
            print("*" * 30)
            continue

        # Start a separate thread to handle incoming messages from this client
        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()


# Log that the server is ready and waiting for connections
print()
print("*" * 30)
print("server is looking for connection...")
print("*" * 30)

# Start listening for client connections
connect_client()
