import sys
import socket
import string
import itertools
my_socket = socket.socket()


# obtaining args and conveying to the right format, then encoding
args = sys.argv
ip_address = args[1]
port = int(args[2])

char_num = list(string.ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# connect
def connect_server():
    address = (ip_address, port)
    my_socket.connect(address)


# send, receive
def get_response():
    '''for i in range(1, 10):
        for password in itertools.product(char_num, repeat=i):
            my_socket.send("".join(password).encode())
            response = my_socket.recv(1024)
            if response.decode() == "Connection success!":
                return "".join(password)
                exit()'''
    f = open('/Users/alcherniaev/PycharmProjects/Password Hacker/passwords.txt', 'r')
    for line in f:
        for password in map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in line.strip('\n')))):
            my_socket.send(password.encode())
            response = my_socket.recv(1024)
            if response.decode() == "Connection success!":
                f.close()
                return password
                exit()


connect_server()
print(get_response())


