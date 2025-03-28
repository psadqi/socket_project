import socket

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server with specified ip address (your computer ip) and port number
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))


def receive():
    """receiving message from server"""

    while True:

        #we need a try except so that our program doesn't crash
        try:

            # receiving information from the server (buffer size is 1024)
            message = client_socket.recv(1024).decode("utf-8")

            #name request
            if message == "what is your name? ":
                print()
                print("*" * 30)
                name = input("please enter your name: ")
                print("*"*30)
                print()
                client_socket.send(name.encode("utf-8"))
            elif message.lower() == "/exit":
                client_socket.close()
                break
            else:
                print(message)

        #if there was an error
        except:
            print("ERROR!")
            client_socket.close()
            break

receive()