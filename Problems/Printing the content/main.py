lib = shelve.open("my_library")
lib["Twilight Saga"] = ["Twilight", "New Moon", "Eclipse", "Breaking Dawn"]

# write your code here
for i in lib:
    print(i + ': ', lib[i])

lib.close()