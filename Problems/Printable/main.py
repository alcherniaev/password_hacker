integer_input = int(input())

if 32 <= integer_input <= 126:
    print(chr(integer_input))
else:
    print(False)
