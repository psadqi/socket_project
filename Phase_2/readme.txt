======================================
Multi-Client Chat Server
======================================

- This project allows multiple clients to connect to a server and communicate independently.
- Each client sends messages to the server, and the server responds by confirming the message.
- The server uses threading to handle multiple clients simultaneously.

======================================
Running the Code
======================================

- First, run the server script (`server.py`).
- Then, run one or more client scripts (`client.py`).
- Each client can send messages to the server.
- To exit, a client should type `/exit`.

======================================
Required Modules
======================================

- This project uses only built-in Python modules:
    - `socket` for network communication.
    - `threading` for handling multiple clients.

======================================
Server (server.py)
======================================

1. **Creating the Server Socket**

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	- Creates a TCP socket using the IPv4 address family (`AF_INET`).
	- Uses `SOCK_STREAM` for a reliable TCP connection.

2. **Binding the Server to an IP and Port**

	server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

	- The server binds to the machine’s local IP address.
	- Uses port `12345` to listen for incoming connections.

3. **Listening for Incoming Connections**

	server_socket.listen()
	print("Server is waiting for connections...\n")

	- Puts the server in listening mode, waiting for client connections.
	- The server prints a message indicating that it is ready.

4. **Handling Client Connections in a Separate Thread**

	def handle_client(client_socket, client_address):

	- Each connected client is assigned a separate thread.
	- This function continuously listens for messages from the client.

5. **Receiving and Processing Messages**

	message = client_socket.recv(1024).decode("utf-8")

	- Receives a message (up to 1024 bytes) from the client.
	- Decodes the received bytes into a string.

6. **Handling Client Exit**

	if message.lower() == "/exit":
	    break

	- If the client sends `/exit`, the connection is closed.
	- The client is removed from the list of connected clients.

7. **Sending a Response to the Client**

	client_socket.send(clients_message.encode("utf-8"))

	- The server confirms receipt of the message by sending a response back to the client.

8. **Accepting Clients in a Loop**

	def connect_client():
	    while True:
	        client_socket, client_address = server_socket.accept()
	        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

	- The server continuously accepts new clients.
	- Each client connection is handled in a separate thread.

======================================
Client (client.py)
======================================

1. **Creating the Client Socket**

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	- The client creates a TCP socket to communicate with the server.

2. **Connecting to the Server**

	client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

	- The client connects to the server’s IP address on port `12345`.

3. **Sending Messages to the Server**

	message = input("message: ")
	client_socket.send(message.encode("utf-8"))

	- The client enters a message, which is encoded and sent to the server.

4. **Handling Client Exit**

	if message.lower() == "/exit":
	    client_socket.close()
	    break

	- If the message is `/exit`, the client disconnects from the server.

5. **Receiving a Response from the Server**

	sent_message = client_socket.recv(1024).decode("utf-8")
	print("\n\t", sent_message, "\n", sep="")

	- The client receives the confirmation message from the server and prints it.

======================================
Summary
======================================

- The server listens for incoming connections and assigns a separate thread for each client.
- Each client can send messages, and the server responds to confirm receipt.
- Clients can disconnect by sending `/exit`.
- The system supports multiple clients communicating independently with the server.

======================================

