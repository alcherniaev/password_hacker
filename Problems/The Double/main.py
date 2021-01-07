import string

double_alphabet = {x: str(x) + str(x) for x in list(string.ascii_lowercase)}
print(double_alphabet)
