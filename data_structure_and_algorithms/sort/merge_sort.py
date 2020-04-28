def merge(left, right):
    """合并左半部分和右半部分"""
    arr = []

    while len(left) and len(right):
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))

    return arr + left + right


def merge_sort(arr):
    """
    归并排序
    稳定性：稳定
    复杂度：
    平均 O(nlog(n))
    最坏 O(nlog(n))
    最好 O(nlog(n))
    """
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


a = [5, 3, 1, 2, 4, 6]
b = merge_sort(a)
print(b)
