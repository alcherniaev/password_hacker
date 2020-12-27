text_ = input()
cipher_ = []
for char in text_:
    # ord - code number assigned to this character
    # chr - convert an integer to the corresponding Unicode character.
    cipher_.append(chr(ord(char) + 1))
print(''.join(cipher_))
