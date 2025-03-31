import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (use the correct server IP address)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

while True:
    #clients message
    message = input("message: ")
    client_socket.send(message.encode("utf-8"))

    # /exit for leaving the server
    if message.lower() == "/exit":
        client_socket.close()
        break

    # Receive message from the server
    sent_message = client_socket.recv(1024).decode("utf-8")
    print("\n\t",sent_message,"\n",sep="")
