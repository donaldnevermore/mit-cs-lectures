for i in range(100, 200):
    r = i % 100 % 10
    if r == 4 or r == 9:
        print(i)
    else:
        print(i, end=' ')
