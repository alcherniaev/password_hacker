import re


regex = '-?[a-zA-Z0-9]?~?_?[^\s^?]' # bad
regex = r'[\w~-]' # better