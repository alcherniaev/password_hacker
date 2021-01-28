import re

template = '[a-fA-F0-9][a-fA-F0-9]?'

print(re.match(template, '1'))