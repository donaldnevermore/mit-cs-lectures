def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        min_value = arr[i]
        j = i + 1

        while j < len(arr):
            if min_value > arr[j]:
                min_index = j
                min_value = arr[j]
            j += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]


a = [5, 1, 4, 3, 2, 6]
select_sort(a)
print(a)
