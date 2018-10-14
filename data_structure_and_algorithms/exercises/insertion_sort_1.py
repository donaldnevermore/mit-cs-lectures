def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        j = i

        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


a = [5, 1, 4, 3, 2, 6]
insertion_sort(a)
print(a)
