def merge(left, right):
    """合并左半部分和右半部分"""
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 把比较大小后剩下的放进去
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


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
        together = merge(left, right)
        return together


a = [5, 3, 1, 2, 4, 6]
b = merge_sort(a)
print(b)
