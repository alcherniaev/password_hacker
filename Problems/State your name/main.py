import re


regex = '-?[\w][\d][\d]?[^\s\w]$'


# playing around with a dict
a = {'a':'22', 'b': '33'}

print(a.get('c', a.get('b')))

print(a.items())