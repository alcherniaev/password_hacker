# work with these variables
def prog():
    rivers = set(input().split())
    states = set(input().split())
    unique_rivers = rivers.difference(states)
    return set(unique_rivers)
print(prog())
