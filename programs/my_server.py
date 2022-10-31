

import socket
from threading import Thread


def return_upper(message):
    message = message.upper()
    print(f"upper case {message}")
    return message


def return_reverse(message):
    message = message[::-1]
    print(f"reverse {message}")
    return message


def return_multiplied(message, times):
    message = message * int(times)
    print(f"multiplied: {message}")
    return message


def split_message(data):
    command = data.split()[0]
    print(f"command: {command}")
    message = " ".join(data.split()[1:])
    print(f"message. {message}")
    return command, message


def modify_message(command, message):
    ret_data = message
    for i in command:
        if i == "u":
            ret_data = return_upper(ret_data)
        elif i == "r":
            ret_data = return_reverse(ret_data)
        elif i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            ret_data = return_multiplied(ret_data, i)
        else:
            print("No command given. ")
    return ret_data


def thread_target(conn, addr):
    # while True:
    with conn:
        print('New thread. Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            command, message = split_message(data)
            print(
                f"Command received: {command}, Message received: {message} ")
            ret_data = modify_message(command, message)
            print(f"ret_data: {ret_data}")
            conn.sendall(ret_data.encode())


def main():
    HOST = '127.0.0.1'
    PORT = 50007

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                Thread(target=thread_target, args=(conn, addr), daemon=True).start()
                print("New thread started")


if __name__ == "__main__":
    main()
