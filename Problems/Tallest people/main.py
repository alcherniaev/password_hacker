def tallest_people(**people):
    height = 0
    for val in people.values():
        if val >= height:
            height = val
    for key, val in sorted(people.items()):
        if val == height:
            print(f'{key} : {val}')
