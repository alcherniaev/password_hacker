import copy


def detect_copy():
    obj = [[1, 2], [3, 4]]
    copy_obj = copying_machine(obj)
    for i, j in zip(obj, copy_obj):
        if id(i) == id(j):
            return "shallow copy"
        else:
            return "deep copy"

FP = 1 / (1 + 1)
