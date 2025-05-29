def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
        # for the first element 2, total = total(=1) X 2 = 2
        # for the second element 4, total = total(which is now 2) X 4 = 8
        # for the third element 8, the new and last total = total(which is now 8) X 8 = 64
    return print(total)


multiply(2, 4, 8)
