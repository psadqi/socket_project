import socket
import threading

#creating the server socket IPV4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server with specified ip address (your computer ip) and port number
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

def send_message():
    """sending message to server"""
    while True:
        message = input("")
        client_socket.send(message.encode("utf-8"))


def receive_message():
    """receiving message from server"""
    while True:
        #we need a try except so that our program doesn't crash
        try:
            # receiving information from the server (buffer size is 1024)
            message = client_socket.recv(1024).decode("utf-8")
            #name request
            if message == "what is your name? ":
                name = input("please enter your name: ")
                client_socket.send(name.encode("utf-8"))
            else:
                print(message)
        #if there was an error
        except:
            print("ERROR!")
            client_socket.close()
            break

#creating threads for sending and receiving messages continuously
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

#starting the send and receiving functions
receive_thread.start()
send_thread.start()
