
======================================
Multi-Client Chat App with Color and GUI
======================================

This project extends a basic chat server into a more advanced system that supports multiple clients with nickname and text color customization. The client uses a graphical user interface (GUI) built with PyQt6. Clients can send public and private messages and see each other's messages styled in their chosen colors.

======================================
Running the Code
======================================

1. **Start the Server**: Run `server.py`. The server will start and wait for incoming connections on port 12345.
2. **Start the Client**: Run `client.py`. Each client will enter a username and choose a color before connecting.
3. **Send Messages**: Clients can send messages to everyone or private messages using `/pm username message`.
4. **Exit the Chat**: Typing `/exit` disconnects the client and informs others.

======================================
Required Modules
======================================

This project uses both built-in and external modules:
- `socket` for network communication.
- `threading` to support concurrent clients.
- `datetime` for timestamps.
- `PyQt6` for the client GUI (`pip install PyQt6`).

======================================
Server (server.py)
======================================

### 1. Creating the Server Socket

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

- Uses IPv4 (AF_INET) and TCP (SOCK_STREAM).
- Binds to the local IP address and port 12345.

### 2. Listening for Incoming Connections

    server_socket.listen()

- Puts the server in listening mode.
- Waits for client connections.

### 3. Accepting Clients and Reading Info

    client_socket, client_address = server_socket.accept()

- Receives the client socket and IP address.
- Client sends a name and color, which are stored in dictionaries.

### 4. Managing Client Info

- Stores client data in two dictionaries:
  - `clients`: maps sockets to (username, color).
  - `username_to_socket`: maps usernames to sockets for private messages.

### 5. Handling Messages

    def receive_message(client_socket):

- Receives messages from a client.
- Handles private messages (`/pm`) and exits (`/exit`).
- Public messages are formatted with username and color.

### 6. Broadcasting to Clients

    def broadcast(message):

- Sends messages to all connected clients.
- Skips disconnected clients automatically.

### 7. Handling Disconnection

- Removes disconnected clients from dictionaries.
- Broadcasts a leave message to all remaining users.

======================================
Client (client.py)
======================================

### 1. Creating the GUI and Socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

- Uses TCP socket to connect to the server.
- GUI is built using PyQt6 with text input, color choice, and display area.

### 2. Connecting to the Server

    client_socket.connect((ip_address, port_number))

- Connects to the server using user input for IP, port, and username.
- Sends the username and color to the server.

### 3. Sending Messages

    def send_message():

- Sends messages to the server.
- If `/exit` is entered, it disconnects the user.

### 4. Receiving Messages

    def receive_message():

- Runs in a background thread.
- Listens for messages and uses PyQt6 signals to display them in the UI.
- Displays messages with HTML color formatting.

### 5. Displaying Messages

    def display_message(message):

- Displays public and private messages.
- Uses HTML and timestamps for visual formatting.

======================================
Features and Summary
======================================

- **Nickname and color selection**: Each client chooses a name and message color.
- **Graphical User Interface**: Built with PyQt6, includes chat box, input field, and controls.
- **Supports private messaging**: Use `/pm username message`.
- **Threaded server**: Handles multiple clients simultaneously.
- **Styled messages**: Messages appear in chosen colors with timestamps.
- **Clean disconnection**: Clients and server handle exit and disconnection smoothly.

This project is a great example of combining network programming with GUI development to create an interactive multi-client chat system.
