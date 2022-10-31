# Echo client program from https://docs.python.org/3/library/socket.html#example

import socket


HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server


def send_message(s):

    command = input("Enter command: ").strip()
    message = input("enter message: ").strip()
    send_msg = command + " " + message

    #send_msg = str(input("Enter input: ")).encode()
    #command = send_msg.decode()[0]
    #message = send_msg.decode()[1:]
    print(f"Command sent: {command} Message sent: {message}")
    s.sendall(send_msg.encode())
    data = s.recv(1024).decode()
    print('Received', repr(data))


MENU_TEXT = """
        Options:
        1 Send_message
        2 Quit1
        """


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connegted to {s}")

        while True:
            print(MENU_TEXT)
            option = input("Enter option: ")
            if option == "1":
                send_message(s)

            elif option == "2":
                s.close()
                exit("Quitting")


if __name__ == "__main__":
    main()
