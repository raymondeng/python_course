# 编写一个UDP客户端，服务端地址为127.0.0.1，端口为51820，发送数据为“Hello, world”

import socket

# Define the server address and port
server_address = ('127.0.0.1', 51820)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the message to the server
message = b'Hello, world'
try:
    sent = sock.sendto(message, server_address)
    if not sent:
        raise Exception("Failed to send message to server")
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
finally:
    # Close the socket
    sock.close()