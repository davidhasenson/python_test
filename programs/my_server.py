from cgitb import reset
import socket

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
                command = data[0]
                message = data[1:]
                print(
                    f"Command received: {command}, Message received: {message} ")
                if command == "u":
                    print(f"upper case {message.upper}")
                    conn.sendall(message.upper().encode())
                elif command == "r":
                    conn.sendall(message[::-1].encode())
                elif command in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    result = data * int(command)
                    conn.sendall(result.encode())
                else:
                    conn.sendall(data.encode())
