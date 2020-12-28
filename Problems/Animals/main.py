animals = open('animals.txt', 'r')
animals_lst = ''.join(animals).replace('\n', ' ')

f = open('animals_new.txt', 'w')
for a in animals_lst:
    f.write(a)

f.close()
animals.close()
