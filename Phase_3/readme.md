---

# Multi-Client Chat Server with Nicknames

This project implements a simple multi-client chat server where clients can connect, send messages, and receive messages from other clients. Each client is required to enter a unique nickname upon joining. The server handles multiple clients simultaneously using threads.

---

## Getting Started

### Prerequisites

This project uses the following built-in Python modules:
- `socket` for network communication.
- `threading` to handle multiple clients concurrently.

### Running the Application

1. **Start the Server**: 
   - Run the server script (`server.py`). The server will begin listening for incoming client connections.

2. **Start the Clients**:
   - Run one or more client scripts (`client.py`). Each client will connect to the server and provide a nickname.

3. **Send Messages**:
   - Clients can send messages, which will be broadcast to all connected clients.

4. **Exit the Chat**:
   - Clients can leave the chat by typing `/exit`, and the server will notify others of the departure.

> **Note**: Clients must enter a username before sending messages. New clients will be prompted to provide a username when they connect.

---

## Server (server.py)

### 1. Creating the Server Socket

```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- `AF_INET`: Uses IPv4 addressing.
- `SOCK_STREAM`: Establishes a reliable TCP connection.

### 2. Binding the Server to an IP and Port

```python
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
```
- The server binds to the local machine's IP address.
- Port `12345` is used for incoming client connections.

### 3. Listening for Incoming Connections

```python
server_socket.listen()
```
- The server listens for client connections on the specified IP and port.

### 4. Handling Client Connections

```python
def connect_client():
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=receive_message, args=(client_socket,)).start()
```
- Accepts new client connections.
- Spawns a new thread to handle communication with each client.

### 5. Receiving Messages from Clients

```python
def receive_message(client_socket):
    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if message == "/exit":
            break
        broadcast(message)
```
- Continuously receives messages from clients.
- If `/exit` is received, the client is disconnected.

### 6. Broadcasting Messages to All Clients

```python
def broadcast(message):
    for client in clients.keys():
        client.send(message)
```
- Sends received messages to all connected clients.
- Notifies clients when someone joins or leaves the chat.

### 7. Handling Client Disconnection

```python
clients.pop(client_socket)
client_socket.close()
```
- Removes the client from the active client list.
- Closes the connection and frees resources.
- Notifies other clients that someone has left.

---

## Client (client.py)

### 1. Creating the Client Socket

```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- Creates a TCP socket for communication with the server.

### 2. Connecting to the Server

```python
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))
```
- The client connects to the server using the local machine's IP and port `12345`.

### 3. Sending Messages to the Server

```python
def send_message():
    while True:
        message = input("")
        if message == "/exit":
            client_socket.close()
            break
        client_socket.send(message.encode("utf-8"))
```
- Clients type messages that are sent to the server.
- If `/exit` is entered, the client disconnects.

### 4. Receiving Messages from the Server

```python
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
```
- Receives messages and prints them.
- When connecting, clients are prompted to provide a nickname.

### 5. Handling Client Disconnection

```python
except:
    print("disconnected!")
    client_socket.close()
    break
```
- Ensures that the client exits gracefully in case of an error or disconnection.

---

## Features and Summary

- **Nickname Requirement**: Clients are prompted to provide a unique nickname when they join.
- **Real-Time Communication**: Messages sent by one client are broadcast to all connected clients.
- **Graceful Exit**: Clients can leave by typing `/exit`, and the server will notify others.
- **Multi-Client Support**: The server uses threading to handle multiple clients concurrently.

This chat server demonstrates the power of socket programming and multi-threading in Python, providing a basic yet effective foundation for building more complex communication systems.