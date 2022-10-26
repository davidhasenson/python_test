# Echo client program from https://docs.python.org/3/library/socket.html#example

from email import message
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server


def send_message():
    send_msg = str(input("E1nter input: ")).encode()
    command = send_msg.decode()[0]
    message = send_msg.decode()
    print(f"Command sent: {command} Message sent: {message}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(send_msg)
        data = s.recv(1024).decode()
    print('Received', repr(data))


MENU_TEXT = """
        Options:
        1 Send_message
        2 Quit1
        """


def main():
    while True:
        print(MENU_TEXT)
        option = input("Enter option: ")
        if option == "1":
            send_message()
        elif option == "2":
            exit("Quitting")


if __name__ == "__main__":
    main()
