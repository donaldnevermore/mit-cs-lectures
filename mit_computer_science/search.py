def search(s, e):
    answer = None
    i = 0
    num_compares = 0
    while i < len(s) and answer is None:
        num_compares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print(answer, num_compares)


count = 0


def bisearch(s, e, first, last):
    global count
    count += 1
    print(first, last, count)
    mid = int(first + (last - first) / 2)
    if last - first <= 1:
        return s[first] == e or s[last] == e  # 简洁的表达
    if s[mid] == e:
        return True
    if s[mid] > e:
        return bisearch(s, e, first, mid - 1)
    else:
        return bisearch(s, e, mid + 1, last)


print(bisearch(range(100000000000), 500, 0, 100000000000))
