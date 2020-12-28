input_ = input()
key_ = int(input())

two_bites = sum((key_).to_bytes(2, 'little'))

message = []
for i in input_:
    message.append(chr(ord(i) + two_bites))

print(''.join(message))


