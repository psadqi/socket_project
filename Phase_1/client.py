#importing the socket module
import socket

#just for fun
import time
import termcolor

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server with specified ip address (your computer ip) and port number
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))
client_socket.send("\n* Hello server *\n********************\n".encode("utf-8"))
message = client_socket.recv(1024).decode("utf-8")
print(message)

#infinite loop for sending and receiving messages
while True:

    # receiving information from the server (buffer size is 1024)
    message = client_socket.recv(1024).decode("utf-8")

    # quiting if the connected client wants to quit else keep sending messages
    if message.lower() == "/exit":
        client_socket.send("/exit".encode("utf-8"))
        print("ending the chat", end=" ")
        time.sleep(0.5)
        print(". ", end="")
        time.sleep(0.5)
        print(". ", end="")
        time.sleep(0.5)
        print(". ", end="")
        break
    else:
        #print(termcolor.colored(message, "green"))
        print(message)
        message = input("message: ")
        client_socket.send(message.encode("utf-8"))

#if we quit from the server
client_socket.close()
print("\nconnection closed successfully")