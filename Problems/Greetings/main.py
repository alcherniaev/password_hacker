def morning(func):
    def wrapper(arg):
        func(arg)
        print(f'Good morning, {arg}')
    return wrapper

@morning
def greetings(name):
    print('Hello,', name)

greetings('Aleksei')
