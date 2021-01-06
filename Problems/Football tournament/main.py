import itertools


teams = ['Best-ever', 'Not-so-good', 'Amateurs']
for game in itertools.combinations(teams, 2):
    print(game)
