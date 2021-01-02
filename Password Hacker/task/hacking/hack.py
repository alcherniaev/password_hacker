import sys
import socket
my_socket = socket.socket()


# obtaining args and conveying to the right format, then encoding
args = sys.argv
ip_address = args[1]
port = int(args[2])
message = args[3].encode()


# connect, send, receive
def get_response():
    address = (ip_address, port)
    my_socket.connect(address)
    my_socket.send(message)
    response = my_socket.recv(1024)
    return response.decode()


print(get_response())
