def binary_search(arr, elem, first, last):
    """牛顿二分查找法"""
    mid = first + (last - first) // 2
    if last - first <= 1:
        return arr[first] == elem or arr[last] == elem  # 简洁的表达
    if arr[mid] == elem:
        return True
    if arr[mid] > elem:
        return binary_search(arr, elem, first, mid - 1)
    else:
        return binary_search(arr, elem, mid + 1, last)


a = [0, 1, 2]
print(binary_search(a, 1, 0, 2))
