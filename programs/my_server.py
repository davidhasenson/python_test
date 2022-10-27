import socket


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


def main():
    HOST = '127.0.0.1'
    PORT = 50007

    while True:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:

                    data = conn.recv(1024).decode()

                    if not data:
                        break
                    command = data.split()[0]
                    print(f"command: {command}")
                    message = " ".join(data.split()[1:])
                    print(f"message. {message}")

                    print(
                        f"Command received: {command}, Message received: {message} ")
                    ret_data = message

                    for i in range(len(command)):
                        if i == "u":
                            ret_data = return_upper(ret_data)
                        elif i == "r":
                            ret_data = return_reverse(ret_data)
                        elif i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            ret_data = return_multiplied(ret_data, i)
                        else:
                            print("No command given. ")

                conn.sendall(ret_data.encode())


if __name__ == "__main__":
    main()
