import itertools
f = open('/Users/alcherniaev/PycharmProjects/Password Hacker/passwords.txt', 'r')
for line in f:
    for password in map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in line.strip('\n')))):
        print(password)

f.close()
'''with open('/Users/alcherniaev/PycharmProjects/Password Hacker/passwords.txt') as f:
    contents = f.read()
    print(contents)

'''
