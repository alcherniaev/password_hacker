# for loop
digit = input()
sum_ = 0
for i in digit:
    sum_ += int(i)

print(sum_)

# or using generators:
print(sum(int(i) for i in digit))
