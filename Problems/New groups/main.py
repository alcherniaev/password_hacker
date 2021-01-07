groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

len_ = int(input())
nums = [int(i) for j in range(len_) for i in [input()]]

while len(groups) != len(nums):
    nums.append(None)

return_dict = dict(zip(groups, nums))
print(return_dict)
