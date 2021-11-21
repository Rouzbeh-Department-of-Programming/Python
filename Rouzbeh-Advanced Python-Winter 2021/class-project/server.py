import socket

IP = '127.0.0.1'
PORT = 12345
messages = []


def handle_client(client):
    message = client.recv(1024).decode()
    print(message)
    server_response = get_server_response(message)
    client.send(server_response.encode())


def get_server_response(message):
    # send/Ali/Hello
    global messages
    message_list = message.split("/")
    if message_list[0] == "send":
        messages.append(message_list[1] + " > " + message_list[2])
        return "Message sent"


server_socket = socket.socket()
print("Socket was created!")
server_socket.bind((IP, PORT))
print("Binding done.")
print("Listening...")
server_socket.listen()
while True:
    client_socket, address = server_socket.accept()
    print("Client connected!")
    handle_client(client_socket)
