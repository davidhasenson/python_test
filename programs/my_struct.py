import struct

# 1. Create a struct format
format_string = "!1500s"

# 2. Create a test data byte e.g

message_to_send = "hello world".encode()  # b'hello world'
bytes_to_send = message_to_send + b"a"*10  # b'aaaaaaaaaa'


# 3. Pack the struct
struct_message = struct.pack(format_string, bytes_to_send)

# 5. Unpack the struct
message, = struct.unpack(format_string, struct_message)

print(message.decode())
print(message[:14].decode(), message[15:])
