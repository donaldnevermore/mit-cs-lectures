def quick_sort(arr):
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
