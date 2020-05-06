def quick_sort(arr):
    """
    快速排序
    稳定性：典型的原地排序是不稳定的
    复杂度：
    平均 O(nlog(n))
    最坏 O(n^2)
    最好 O(nlog(n))
    """
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr.pop(pivot_index)
    left = []
    right = []

    for i in arr:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


a = [5, 1, 4, 3, 2, 6]
b = quick_sort(a)
print(b)
