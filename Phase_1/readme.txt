Simple Client-Server Chat Application

- only one client
- only one message can be sent each time by the client
- server sends the first message

======================================
running the code
======================================

- you must run the server.py at first and then client.py file after it

    warning!
        - you can only run it once and after that you must ensure that you have terminate the program before
          running it again because if it isn't terminate you cant run it again because the port it busy with
          the last connection

- if you want to have a better experience run it in cmd instead of vs code or pycharm so that you dont have to change
  between terminals for each message

  - run cmd twice in the directory first run server.py file using " py server.py " command and after that
    run client.py in the second cmd using " py client.py "

  - !!! if you are using cmd it doesnt support the color !!! 
	- comment the print function that has color in the loop and remove the simple print out of comment

======================================
Required Module
======================================

This project requires the **termcolor** module. Since it's not a built-in module, you need to install it first using the following command:

    pip install termcolor

======================================
Server (server.py)
======================================

1. **Binding the Server**

    server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

    - The server must be bound to a specific IP address and port number.
    - We retrieve the computer’s IP address using a built-in method from the `socket` module.
    - This avoids manually entering the IP for every machine running the code.
    - A port number is required. Using a high number is recommended since low ones are often reserved for system processes.

2. **Listening for Connections**

    server_socket.listen()

    - The server enters a listening state to allow clients to connect.

    client_socket, client_address = server_socket.accept()

    - Accepts an incoming connection.
    - The `accept()` method returns:
      - `client_socket`: A socket object for communication.
      - `client_address`: The IP address of the client (same as the server in this case).

3. **Sending a Welcome Message**

    client_socket.send("\n* hello client *\n********************\n".encode("utf-8"))

    - This informs the client of a successful connection.
    - Messages must be encoded before sending (UTF-8 is used by default).
    - there is a same message from client sent to server "\n* Hello server *\n********************\n"

4. **Handling Continuous Communication**

    while loop:

        message = client_socket.recv(1024).decode("utf-8")

        - The `recv(1024)` method receives messages with a buffer size of 1024 bytes.
        - the buffer size can have any length because in tcp connection the transmission of message is guaranteed
            but if the buffer size is less than the message size the messages receives in seperated parts
        - Received data is in bytes, so we decode it using UTF-8.

5. **Handling Messages with If-Else**

    if message.lower() == "/exit":
        server_socket.close()

        - If the message is "/exit", the connection is closed.

    else:

        print(termcolor.colored(message, "blue"))
        message = input("Message: ")
        client_socket.send(message.encode("utf-8"))

        - If the message isn't "/exit", it is displayed in blue.
        - The user enters a response, which is sent to the client.

======================================
Client (client.py)
======================================

- The client works similarly to the server, except for one key difference:

    client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

    - The client does not bind itself to an IP and port.
    - It connects to the server’s IP and port.

- Once connected, the client executes:

    client_socket.send("You have connected to the server".encode("utf-8"))

    - This sends a confirmation message to the server.

======================================
Summary
======================================

- The server listens for connections, accepts clients, and keeps communication ongoing.
- The client connects to the server and sends messages.
- Both the server and client use UTF-8 encoded messages.
- If either side sends "quit", the connection is closed.

======================================
End of File
======================================
