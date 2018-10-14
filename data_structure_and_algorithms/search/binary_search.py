# 牛顿二分查找法
def bisearch(s, e, first, last):
    global count
    count += 1
    print(first, last, count)
    mid = int(first + (last - first) / 2)
    if last - first <= 2:
        return s[first] == e or s[last] == e  # 简洁的表达
    if s[mid] == e:
        return True
    if s[mid] > e:
        return bisearch(s, e, first, mid - 1)
    else:
        return bisearch(s, e, mid + 1, last)
