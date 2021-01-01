import sys
args = sys.argv
'''# further code of the script "process_four_numbers.py"
if len(args) == 5:
    for i in range(1, 5):
        args[i] = int(args[i])
    print(args[1:5])
else:
    print("The script should be called with four arguments")'''
my_list = [int(arg) for arg in args[1:5]]
print(my_list)
