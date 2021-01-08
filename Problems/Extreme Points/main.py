#test_dict = json.loads(input())
test_dict = {"a": 43, "b": 1233, "c": 8}
# Work with the 'test_dict'

min_ = min(test_dict, key=test_dict.get)
max_ = max(test_dict, key=test_dict.get)
print("min: " + str(min_) + "\n" + "max: " + str(max_))
