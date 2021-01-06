import itertools


main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

for a, b, c in itertools.product(zip(main_courses, price_main_courses),
                                 zip(desserts, price_desserts),
                                 zip(drinks, price_drinks)):
    receipt = (int(a[1]) + int(b[1]) + int(c[1]))
    if receipt <= 30:
        print(a[0], b[0], c[0], receipt)
