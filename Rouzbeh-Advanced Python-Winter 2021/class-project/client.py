import socket

IP = '127.0.0.1'
PORT = 12345


def send_to_server(message):
    client_socket = socket.socket()
    client_socket.connect((IP, PORT))
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response


def run_menu(name):
    command = int(input(
        "Choose one of the options:\n" +
        "1.Send message\n" +
        "2.Refresh\n" +
        "3.Exit\n"
    ))
    handle_command(command, name)


def handle_command(command, name):
    if command == 1:
        message = input("Enter your message:")
        to_send = "send" + "/" + name + "/" + message
        response = send_to_server(to_send)
        print(response)


name = input("Enter you name:")
while True:
    run_menu(name)
