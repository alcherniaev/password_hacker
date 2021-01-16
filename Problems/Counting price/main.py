def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper  

@price_string
def new_price(val):
    return val * 0.9


print(new_price(196))
