======================================
Multi-Client Chat Server with Nicknames
======================================

This project implements a simple chat server that allows multiple clients to connect,
send messages, and receive messages from other clients. Each client is required to enter a nickname
when they join. The server handles multiple clients simultaneously using threads.

======================================
Running the Code
======================================

1. **Start the Server**: Run the server script (`server.py`). The server will listen for incoming client connections.
2. **Start the Clients**: Run one or more client scripts (`client.py`). Each client will connect to the server and enter a nickname.
3. **Send Messages**: Clients can send messages, which will be broadcasted to all connected clients.
4. **Exit the Chat**: Clients can leave by typing `/exit`, and the server will notify others.

*** you must enter the username of a client then a new client can enter username and start sending message***

======================================
Required Modules
======================================

This project only uses built-in Python modules:
- `socket` for network communication.
- `threading` for handling multiple clients concurrently.

======================================
Server (server.py)
======================================

### 1. Creating the Server Socket


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


- `AF_INET`: Uses IPv4 addressing.
- `SOCK_STREAM`: Establishes a reliable TCP connection.

### 2. Binding the Server to an IP and Port


    server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))


- The server binds to the machine’s IP address.
- Uses port `12345` for incoming connections.

### 3. Listening for Incoming Connections


    server_socket.listen()


- The server starts listening for client connections.
- Clients can connect by specifying the same IP and port.

### 4. Handling Client Connections


    def connect_client():
        while True:
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=receive_message, args=(client_socket,)).start()


- Accepts client connections.
- Starts a new thread for each client.

### 5. Receiving Messages from Clien
```
    def receive_message(client_socket):


- Continuously receives messages from a client.
- If the client sends `/exit`, they are disconnected.

### 6. Broadcasting Messages to All Clients


    def broadcast(message):
        for client in clients.keys():
            client.send(message)


- Sends messages to all connected clients.
- Notifies all clients when someone joins or leaves.

### 7. Handling Client Disconnection


    clients.pop(client_socket)
    client_socket.close()


- Removes the client from the active list.
- Closes the client’s connection to free resources.
- Notifies other clients that someone left.

======================================
Client (client.py)
======================================

### 1. Creating the Client Socket


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


- Creates a TCP socket for communication with the server.

### 2. Connecting to the Server


    client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))


- The client connects to the server’s IP and port `12345`.

### 3. Sending Messages to the Server


    def send_message():
        while True:
            message = input("")
            if message == "/exit":
                client_socket.close()
                break
            client_socket.send(message.encode("utf-8"))


- The client types a message, which is sent to the server.
- If `/exit` is entered, the client disconnects.

### 4. Receiving Messages from the Server


    def receive_message():
        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")
                if message == "what is your name? ":
                    name = input("please enter your name: ")
                    client_socket.send(name.encode("utf-8"))
                else:
                    print(message)
            except:
                print("disconnected!")
                client_socket.close()
                break


- Receives messages and prints them.
- When first connecting, the client is asked to provide a name.

### 5. Handling Client Disconnection


    except:
        print("disconnected!")
        client_socket.close()
        break


- Ensures the client exits gracefully if an error occurs.

======================================
Features and Summary
======================================

- **Clients provide a nickname upon joining**: Each client is identified by a unique name.
- **Messages are broadcasted to all clients**: Everyone in the chat sees messages in real-time.
- **Clients can leave by sending `/exit`**: The server and other clients are notified when someone leaves.
- **The server handles multiple clients using threads**: Each client runs in a separate thread, allowing simultaneous communication.

This chat server is a simple yet powerful way to understand socket programming and multi-threaded server handling in Python.

