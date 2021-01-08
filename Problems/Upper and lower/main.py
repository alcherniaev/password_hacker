some_iterable = input().split()

dict_ = {word.upper(): word.lower() for word in some_iterable}
print(dict_)
