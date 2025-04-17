```markdown
# Simple Client-Server Chat Application

A basic chat application demonstrating socket programming in Python, allowing communication between a single client and server.

---

## 📚 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Server Implementation](#server-implementation)
  - [Client Implementation](#client-implementation)
- [Technical Details](#technical-details)
- [Limitations](#limitations)
- [License](#license)

---

## 🚀 Features
- TCP/IP socket communication
- Simple text-based chat interface
- Graceful connection termination with `/exit` command
- Cross-platform compatibility

---

## ⚙️ Installation

### Prerequisites
- Python 3.x
- pip package manager

### Dependencies
Install the required dependency:

```bash
pip install termcolor
```

---

## ▶️ Usage

1. First, start the server:
```bash
python server.py
```

2. Then, in a separate terminal, start the client:
```bash
python client.py
```

3. Type and send messages. To exit:
```
/exit
```

### ⚠️ Notes:
- Use separate terminal windows for server and client.
- CMD or PowerShell may not support `termcolor` — comment out colored lines if needed.
- Ensure previous instances are terminated before restarting to avoid port conflicts.
- For CMD users: comment `termcolor` lines and uncomment simple print statements.

---

## 🧠 Code Explanation

### 🖥️ Server Implementation (`server.py`)

#### 1. Socket Creation and Binding

```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
```

- Creates a TCP socket using IPv4.
- Binds to the computer’s IP on port `12345`.

#### 2. Listening for Connections

```python
server_socket.listen()
client_socket, client_address = server_socket.accept()
```

- Enters listening mode.
- Accepts a client connection and returns a communication socket.

#### 3. Sending Initial Message

```python
client_socket.send("\\n* hello client *\\n********************\\n".encode("utf-8"))
```

- Sends a welcome message encoded in UTF-8.

#### 4. Chat Loop

```python
while True:
    message = client_socket.recv(1024).decode("utf-8")
    if message.lower() == "/exit":
        break
    else:
        print(message)
        message = input("message: ")
        client_socket.send(message.encode("utf-8"))
```

- Receives messages with a 1024-byte buffer.
- Handles `/exit` for disconnection.
- Otherwise, prints and responds to messages.

---

### 💻 Client Implementation (`client.py`)

#### 1. Connecting to the Server

```python
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))
client_socket.send("\\n* Hello server *\\n********************\\n".encode("utf-8"))
```

- Connects to the server IP and port.
- Sends an initial greeting.

#### 2. Chat Loop

```python
while True:
    message = client_socket.recv(1024).decode("utf-8")
    if message.lower() == "/exit":
        break
    else:
        print(message)
        message = input("message: ")
        client_socket.send(message.encode("utf-8"))
```

- Identical to the server’s loop.
- Sends and receives messages using UTF-8.

---

## 🔍 Technical Details

### Key Points:
- TCP ensures reliable message delivery.
- UTF-8 is used for consistent text encoding.
- A 1024-byte buffer handles small message sizes.
- Port `12345` should not be used by another service.

### Communication Flow:
1. Server binds and listens.
2. Client connects.
3. Both parties exchange messages.
4. Chat ends when `/exit` is entered.

---

## ❌ Limitations
- Only supports one client at a time.
- No message history or logging.
- No user authentication.
- No reconnection or timeout logic.
- No encryption or secure transport.

---

## 📝 License

This project is open-source and intended for educational purposes.  
No official license has been declared.
```