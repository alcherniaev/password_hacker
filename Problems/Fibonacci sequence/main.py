def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        list_ = [0, 1]
        while len(list_) < n:
            list_.append(sum([list_[-1], list_[-2]]))
        for i in list_:
            yield i
